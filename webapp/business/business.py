from webapp.models import *
import jdatetime
import datetime
from datetime import timedelta
from django.db import connection
class Utils:
    @staticmethod
    def getDate(dt):


        y=str(dt).split("-")
        if(len(y)==3):
            year=int(y[0])
            month=int(y[1])
            day=int(y[2])
            return jdatetime.date(year,month,day).togregorian()
        else:
            return datetime.date.today()
    @staticmethod
    def getTitleDate(dt=None):
        if(dt == None):
            return jdatetime.date.today()
        else:
            return dt

    @staticmethod
    def getAmarReportByDate(dt=None):
        if (dt is None):
            maxDate=Amar.objects.raw("select max(timestamp) as id from amar")
            try:

                company=Amar.objects.filter(timestamp=maxDate[0].id)
            except IndexError:
                company=Amar.objects.all()
            return company
        else:
                company=Amar.objects.filter(timestamp=Utils.getDate(dt))
                return company
    @staticmethod
    def getBedehReportByDate(dt=None):
         if (dt is None):

             maxDate=Bedehkar.objects.raw("select max(timestamp) as id from bedehkar")
             try:
                 #print(maxDate[0].id)

                 company=Bedehkar.objects.filter(timestamp=maxDate[0].id)
             except IndexError:
                 company=Bedehkar.objects.all()
             #print(company[0].id)
             return company
         else:
                 company=Bedehkar.objects.filter(timestamp=Utils.getDate(dt))
                 return company
    @staticmethod
    def getHazineReportByDate(dt=None):
          if (dt is None):
              maxDate=Hazine.objects.raw("select max(timestamp) as id from hazine")
              try:
                  company=Hazine.objects.filter(timestamp=maxDate[0].id)
              except IndexError:
                  company=Haizne.objects.all()
              return company
          else:
                  company=Hazine.objects.filter(timestamp=Utils.getDate(dt))
                  return company

    @staticmethod
    def getTalabReportByDate(dt=None):
         if (dt is None):
             maxDate=Talab.objects.raw("select max(timestamp) as id from talab")
             try:

                 company=Talab.objects.filter(timestamp=maxDate[0].id)
             except IndexError:
                 company=Talab.objects.all()
             return company
         else:
                 company=Talab.objects.filter(timestamp=Utils.getDate(dt))
                 return company
    @staticmethod
    def getSumAmarByDate(dt=None):
        company=Utils.getAmarReportByDate(dt)
        sum=0
        for i , c in enumerate(company):
            sum+=float(company[i].getMeghdar())*float(company[i].getFi())

        return sum
    @staticmethod
    def getSumTalabByDate(dt=None):
         company=Utils.getTalabReportByDate(dt)
         sum=0
         for i , c in enumerate(company):
             sum+=float(company[i].getMeghdar())

         return sum

    @staticmethod
    def getSumBedehByDate(dt=None):
        company=Utils.getBedehReportByDate(dt)
        sum=0
        for i , c in enumerate(company):
            sum+=float(company[i].getMeghdar())

        return sum
    @staticmethod
    def getSumHazineByDate(dt=None):
        company=Utils.getHazineReportByDate(dt)
        sum=0
        for i , c in enumerate(company):
            sum+=float(company[i].getMeghdar())

        return sum


    @staticmethod
    def getMojudiAlyaf(dt=None):

        if (dt is None):
             maxDate=Amar.objects.raw("select max(timestamp) as id from amar")
             #print("31321")
             try:


                 company=Amar.objects.filter(timestamp=maxDate[0].id)
                 print(company[0].id)
             except IndexError:

                 company=0
             return company
        else:

                 company=Amar.objects.filter(timestamp=getDate(dt))
                 return company
    @staticmethod
    def getSumMojudiAlyaf(dt=None):
        company=Utils.getMojudiAlyaf(dt)

        sum=0.0

        for i , c in enumerate(company):
            sum+=float(company[i].getMeghdar())

        return sum
    @staticmethod
    def get_N_Bedehkar():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Bedehkar.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from bedehkar group by (pmonth(timestamp))")
       return company
    @staticmethod
    def get_N_Bestankar():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Talab.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from talab group by (pmonth(timestamp))")
       return company
    @staticmethod
    def get_N_Mahsool():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Amar.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from amar group by (pmonth(timestamp))")
       return company

    @staticmethod
    def get_N_Hazine():
         #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


        company=Talab.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from hazine group by (pmonth(timestamp))")
        return company

    @staticmethod
    def get_Nakh():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Amar.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from amar where Mahsool_id  in (select id from mahsool where mahsoolName like '%نخ%') group by (pmonth(timestamp))")
       return company
    @staticmethod
    def get_Alyaf():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Amar.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from amar where Mahsool_id  in (select id from mahsool where mahsoolName like '%الیاف%') group by (pmonth(timestamp))")
       return company
    @staticmethod
    def get_Zayeat():
        #m1=Bedehkar.objects.raw("select sum(meghdar)as id,timestamp from bedehkar where pmonth(timestamp)=1 group by timestamp  ")


       company=Amar.objects.raw("select sum(meghdar) as id,pmonth(timestamp) as month from amar where Mahsool_id  in (select id from mahsool where mahsoolName like '%ضا%') group by (pmonth(timestamp))")
       return company
    @staticmethod
    def getCurrentNakh():

            maxDate=Amar.objects.raw("select max(timestamp) as id from amar")
            try:

                company=Amar.objects.raw("select sum(meghdar) as id from amar where timestamp='{0}' and mahsool_id in (select id from mahsool where mType=0)".format(maxDate[0].id))

            except IndexError:
                company=Amar.objects.all()
            return company[0].id if company[0].id is not None else 0
    @staticmethod
    def getCurrentZayeat():

            maxDate=Amar.objects.raw("select max(timestamp) as id from amar")
            try:

                company=Amar.objects.raw("select sum(meghdar) as id from amar where timestamp='{0}' and mahsool_id in (select id from mahsool where mType=2)".format(maxDate[0].id))

            except IndexError:
                company=Amar.objects.all()

            return company[0].id if company[0].id is not None else 0

    @staticmethod
    def getCurrentAlyaf():

             maxDate=Amar.objects.raw("select max(timestamp) as id from amar")

             try:

                 company=Amar.objects.raw("select sum(meghdar) as id from amar where timestamp='{0}' and mahsool_id in (select id from mahsool where mType=1)".format(maxDate[0].id))

             except IndexError:
                 company=Amar.objects.all()
             return company[0].id if company[0].id is not None else 0
################################## Hazine ###################################
    @staticmethod
    def getListHazineLastWeek():
        lastweek=Hazine.objects.raw("select id,meghdar,timestamp,hazineName_id from hazine where pmonth(CURRENT_DATE)=pmonth(timestamp) and floor(pday(timestamp)/7)=floor(pday(CURRENT_DATE)/7)")
        return lastweek
    @staticmethod
    def getListHazineLastMonth():
        lastmonth=Hazine.objects.raw("select id,meghdar,timestamp,hazineName_id from hazine where pmonth(CURRENT_DATE)=pmonth(timestamp)")
        return lastmonth
########################## Talab #######################################

    @staticmethod
    def getListTalabLastWeek():
        lastweek=Talab.objects.raw("select id,meghdar,timestamp,talabName_id from talab where pmonth(CURRENT_DATE)=pmonth(timestamp) and floor(pday(timestamp)/7)=floor(pday(CURRENT_DATE)/7)")
        return lastweek
    @staticmethod
    def getListTalabLastMonth():
        lastmonth=Talab.objects.raw("select id,meghdar,timestamp,talabName_id from talab where pmonth(CURRENT_DATE)=pmonth(timestamp)")
        return lastmonth


########################## Bedeh #######################################

    @staticmethod
    def getListBedehkarLastWeek():
        lastweek=Bedehkar.objects.raw("select id,meghdar,timestamp,bedehkarName_id from bedehkar where pmonth(CURRENT_DATE)=pmonth(timestamp) and floor(pday(timestamp)/7)=floor(pday(CURRENT_DATE)/7)")
        return lastweek
    @staticmethod
    def getListBedehkarLastMonth():
        lastmonth=Bedehkar.objects.raw("select id,meghdar,timestamp,bedehkarName_id from bedehkar where pmonth(CURRENT_DATE)=pmonth(timestamp)")
        return lastmonth

########################## Amar #######################################

    @staticmethod
    def getListAmarLastWeek():
        lastweek=Amar.objects.raw("select id,meghdar,fi,timestamp,Mahsool_id from amar where pmonth(CURRENT_DATE)=pmonth(timestamp) and floor(pday(timestamp)/7)=floor(pday(CURRENT_DATE)/7)")
        return lastweek
    @staticmethod
    def getListAmarLastMonth():
        lastmonth=Amar.objects.raw("select id,meghdar,fi,timestamp,Mahsool_id from amar where pmonth(CURRENT_DATE)=pmonth(timestamp)")
        return lastmonth
