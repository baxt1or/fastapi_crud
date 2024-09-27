from models import Item
from sqlalchemy.orm import Session
from db import logger
from sqlalchemy.exc import SQLAlchemyError


def create_item(name:str, description:str, price:float,db:Session):
    """ 
    Creates an item instance from database

    Args:
        name: str -> Name of the item
        description: str -> Description of the item
        price: float -> Price of the item

    Returns:
         The instance of the item

    Raises:
        ValueError: if the item  not being created

    """
    try:
        item = Item(name=name, description=description, price=price)
        db.add(item)
        db.commit()
        db.refresh(item)
        logger.info(f"Item {name} has created successfully.")
        return item
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Failed to create an item {e}")
        raise ValueError("Failed to create the item. Please check the input data")


# Fetchs All the Items from the database
def get_items(db:Session):
    """ 
    Fetchs all the items from a database.

    Args:
      db : Session -> Database session

    Returns:
       All the items that has been created so far

    Raises: 
       SQlAlchemyError: If an error occurs while fetching items data
    """
    try:
        items = db.query(Item).all()

        if not items:
            logger.info("No Items found")
            return []
        return items
    
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"failed to get items {e}")
        raise ValueError("failed to get items")