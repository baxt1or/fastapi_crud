from fastapi import APIRouter, Depends, status, HTTPException
from db import get_db
from services import create_item, get_items
from schemas import ItemRequestSchema, ItemResponseSchema
from sqlalchemy.orm import Session
from db import logger
from sqlalchemy.exc import SQLAlchemyError
from typing import List

# Iniitaling the fastapi Item routes
router = APIRouter()

# Post endpoint to post an item instance to database
@router.post("/", response_model=ItemResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_one(item : ItemRequestSchema,db: Session = Depends(get_db)):

    """  
    Create item endpoint that creates an item instance to database

    Args:
       item : ItemRequestSchema -> Item data schema to pass as a request body
       db : Session -> Database session, injected bt FastAPI
    
    Returns:
       item as response
    
    Raises:
        HTTPException: if the creation is not successful

    """
    
    try:
        new_item = create_item(name=item.name, 
                       description=item.description, 
                       price=item.price, 
                       db=db)
        logger.info(f"Item {new_item.name} has been created successfully")
        return new_item
    
    except SQLAlchemyError as e:

        logger.error(f"failed to create an item: {str(e)}")

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to create an item")


# Get enpoint to fetch the item data
@router.get("/", response_model=List[ItemResponseSchema], status_code=status.HTTP_200_OK)
async def get_many(db: Session = Depends(get_db)):
    """ 
    Fetchs all the data from a database for client

    Args: 
      db: Session -> Database Sesson, injerted by FastAPI

    Returns:
       Fetchs all the item data as JSON format

    Raises:
       HTTPExpection: if an error occurs while fetching the data items
    """

    try:
        items = get_items(db=db)

        if not items:
            logger.info("No items created yet.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items created yet.")
        return items
    except SQLAlchemyError as e:
        logger.error(f"failed to fetch items: {str(e)}")

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to fetch items")
        
  