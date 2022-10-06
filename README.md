# get requirement.txt 
pip3 freeze > requirements.txt 

# run app
uvicorn main:app --reload

# altertable
ALTER TABLE mail_10_minutes.email
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;