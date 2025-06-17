from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, Identity
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List

DATABASE_URL = "postgresql://ecommerce:Zeus_3245@localhost/ecommerce"

