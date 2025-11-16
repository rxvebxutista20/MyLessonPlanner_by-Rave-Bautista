import argparse
import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
import uuid
from datetime import datetime, timezone

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(email: str, name: str, password: str):
    mongo_url = os.environ.get('MONGO_URL')
    db_name = os.environ.get('DB_NAME')
    if not mongo_url or not db_name:
        raise RuntimeError('MONGO_URL and DB_NAME must be set in .env or environment')

    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]

    existing = await db.users.find_one({'email': email})
    if existing:
        print(f"User already exists: {email}")
        client.close()
        return

    hashed = pwd_context.hash(password)
    user = {
        'id': str(uuid.uuid4()),
        'email': email,
        'name': name,
        'password': hashed,
        'created_at': datetime.now(timezone.utc).isoformat()
    }

    result = await db.users.insert_one(user)
    print('✓ User created')
    print(f'  email: {email}')
    print(f'  name: {name}')
    print(f'  inserted_id: {result.inserted_id}')

    client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new user in MongoDB')
    parser.add_argument('--email', required=False, help='Email address for the user')
    parser.add_argument('--name', required=False, help='Display name for the user')
    parser.add_argument('--password', required=False, help='Plaintext password (will be hashed)')
    parser.add_argument('--default', action='store_true', help='Create the default admin user (Ravebautista)')

    args = parser.parse_args()

    # If --default is specified, create a default admin user with preset credentials
    if args.default:
        default_email = 'rxvebxutista@gmail.com'
        default_name = 'Ravebautista'
        default_password = 'Bautista_03202000'
        print('Creating default user:')
        print(f'  name: {default_name}')
        print(f'  email: {default_email}')
        asyncio.run(create_user(default_email, default_name, default_password))
    else:
        # If not using default, require the explicit fields
        if not args.email or not args.name or not args.password:
            parser.error('When not using --default you must pass --email, --name and --password')
        asyncio.run(create_user(args.email, args.name, args.password))
