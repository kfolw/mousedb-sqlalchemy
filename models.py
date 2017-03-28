from app import db 

from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class Cage(Base):
	 __tablename__ = 'cages'

	cage_id = Column(Integer(), primary_key=True)
   	cage_number = Column(Integer(), index=True)
    	genotype = Column(String(255))
    	sex = Column(String(255))
    	quantity = Column(Integer())
    	dob = Column(DateTime(), default=datetime.now)
    	injured = Column(Boolean(), default=False)


    	def __init__(self, number, genotype, sex, quantity=0, dob, injured):
        	self.cage_number = number
        	self.genotype = genotype
        	self.sex = sex
        	self.quantity = quantity
        	self.dob = dob
        	self.injured = injured

    	def __repr__(self):
        		return "Cage(cage_number='{self.cage_number}', " \
                  	     	"genotype='{self.genotype}', " \
                       		"sex='{self.sex}', " \
                       		"quantity={self.quantity}, " \
                       		"DOB={self.dob}," \
                      		 "injured={self.injured})".format(self=self)


class Record(Base):
	__tablename__ = 'records'

	record_id = Column(Integer(), primary_key=True)
	date = Column(DateTime(), default=datetime.now)
	notes = Column(String(255))
	cage_id = Column(Integer(), ForeignKey('cages.cage_id'))
	cage = relationship('Cage', backref=backref('records', order_by=record_id))

	def __repr__(self):
		return "Record(record_id={self.record_id}, " \
                     		 "date={self.date}", \
                     		 "notes={self.notes})".format(self=self)
