from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from core.config import settings
from db.session import get_db
from core.hashing import Hasher
from db.repositary.login import get_user_by_email
from core.security import create_access_token

router = APIRouter()

def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


oauth_scheme = OAuth2PasswordBearer(
   
    tokenUrl="/token"
)


def get_current_user(token:str=Depends(oauth_scheme),db:Session=Depends(get_db)):
    credential_exception=HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail="detail=Could not validiate credintials,please login again"
    )

    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        email:str=payload.get("sub")
        if email is None:
            raise credential_exception
    except JWTError:
        raise credential_exception  


    user=get_user_by_email(email=email,db=db)
    if user is None:
        raise credential_exception

    return user    

