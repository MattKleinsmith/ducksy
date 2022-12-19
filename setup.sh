echo "SECRET_KEY=replace_with_a_key_just_for_demo_purposes" >> .env
echo "FLASK_RUN_PORT=5001" >> .env
echo "DATABASE_URL=sqlite:///dev.db" >> .env

npm install --prefix react-app
npm run build --prefix react-app
pip install -r requirements.txt
flask db upgrade
flask seed all

flask run
