from django.db import models
from django.utils.timezone import now
from datetime import datetime
# Create your models here.
class employee(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    def __str__(self):
        return self.firstName
class alyaf_kham_va_rangshode(models.Model):
    #title=models.CharField("الیاف خام و رنگ شده",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateField(auto_now_add=True,unique=True)
    class Meta:
        db_table="alyaf_kham_va_rangshode"
class alyaf_daraje2_18(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateField(auto_now_add=True,unique=True)
    class Meta:
        db_table="alyaf_daraje2_18"

class alyaf_jaryan_18(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="alyaf_jaryan_18"

class alyaf_jaryan_30(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="alyaf_jaryan_30"

class alyaf_jaryan_36(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="alyaf_jaryan_36"

class nakh_18(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="nakh_18"

class nakh_2_18(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="nakh_2_18"

class nakh_24(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="nakh_24"

class nakh_30(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="nakh_30"

class nakh_36(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="nakh_36"

class zayeat(models.Model):
    #title=models.CharField("الیاف درجه دو در جریان ریسندگی جهت نمره 18",max_length=60)
    meghdar=models.FloatField("مقدار(کیلوگرم)")
    fi=models.FloatField("فی هر کیلوگرم")
    val=models.FloatField("ارزش ریال")
    timestamp=models.DateTimeField(auto_now_add=True,unique=True)
    class Meta:
        db_table="zayeat"
class bestankari(models.Model):
    ashkhas=models.DecimalField("بستانکاری خاطره از اشخاص",max_digits=12, decimal_places=0)
    bank=models.DecimalField("بانک",max_digits=12, decimal_places=0)
    class Meta:
        db_table="bestankari"
class bedehkari(models.Model):
    ashkhas=models.DecimalField("بدهکاری خاطره به اشخاص",max_digits=12, decimal_places=0)
    bank=models.DecimalField("بانک",max_digits=12, decimal_places=0)
    class Meta:
        db_table="bedehkari"
'''
class Tolid(models.Model):
    meghdarAlyaf=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf18=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf18=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf30=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf30=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf36=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf36=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarNakh18=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiNakh18=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarNakh18_2=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiNakh18_2=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarNakh24=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiNakh24=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdar=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf=models.FloatField("فی هر کیلوگرم",blank=True,null=True)

    meghdarAlyaf=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fiAlyaf=models.FloatField("فی هر کیلوگرم",blank=True,null=True)
'''
class Mahsool(models.Model):
    mahsooltype=(
    (0,'نخ'),
        (1 ,'الیاف'),
        (2,'ضایعات'),
        )
    mahsoolName=models.CharField("نام کالا",max_length=100)
    mType=models.IntegerField("نوع کالا",choices=mahsooltype)
    def __str__(self):
        return self.mahsoolName
    class Meta:
        db_table="mahsool"

class Amar(models.Model):
    Mahsool=models.ForeignKey(Mahsool,on_delete=models.CASCADE)
    meghdar=models.FloatField("مقدار(کیلوگرم)",blank=True,null=True)
    fi=models.FloatField("فی هر کیلوگرم",blank=True,null=True,default=0)
    timestamp=models.DateField(auto_now_add=True);

    def total(self):
        if(self.fi !=  None and self.meghdar != None):
            return format((self.fi*self.meghdar),",.0f")
        return 0.0
    def getMeghdar(self):
         if(self.meghdar !=  None ):
             return "{}".format(self.meghdar)
             #return 1
         return 0.0
    def getFi(self):
         if(self.fi !=  None ):
             return "{}".format(self.fi)
         return 0.0
    def getFiFloat(self):
         if(self.fi !=  None ):
             return format(self.fi,",.0f")
         return 0.0
    class Meta:
        db_table="amar"
class BedehkarType(models.Model):
    bedehkarName=models.CharField("نام بدهکاری",max_length=100)
    def __str__(self):
       return "{}".format(self.bedehkarName)
    class Meta:
        db_table="bedehkartype"
class Bedehkar(models.Model):
    bedehKarName=models.ForeignKey(BedehkarType,verbose_name="نوع",on_delete=models.CASCADE)
    meghdar=models.FloatField("مبلغ بدهکاری",blank=True,null=True,default=0)

    timestamp=models.DateField(auto_now_add=True)
    def getMeghdar(self):
         if(self.meghdar !=  None ):
             return "{}".format(self.meghdar)
         return "0"
    def getMeghdarCurrency(self):
        if(self.meghdar !=  None ):
            return format(self.meghdar,",.0f")
        return "0"

    class Meta:
        db_table="bedehkar"



class TalabType(models.Model):
    talabName=models.CharField("نام طلب",max_length=100)
    def __str__(self):
       return "{}".format(self.talabName)
    class Meta:
        db_table="talabtype"
class Talab(models.Model):
    talabName=models.ForeignKey(TalabType,verbose_name="نوع",on_delete=models.CASCADE)
    meghdar=models.FloatField("مبلغ بدهکاری",blank=True,null=True,default=0)
    timestamp=models.DateField(auto_now_add=True);
    def getMeghdar(self):
         if(self.meghdar !=  None ):
             return "{0:.0f}".format(self.meghdar)
    def getMeghdarCurrency(self):
        if(self.meghdar !=  None ):
            return format(self.meghdar,",.0f")
        return "0"
    class Meta:
        db_table="talab"



class HazineType(models.Model):
    hazineName=models.CharField("نام هزینه",max_length=100)
    def __str__(self):
       return "{}".format(self.hazineName)
    class Meta:
        db_table="hazinetype"
class Hazine(models.Model):
    hazineName=models.ForeignKey(HazineType,verbose_name="نوع",on_delete=models.CASCADE)
    meghdar=models.FloatField("مبلغ",blank=True,null=True,default=0)
    timestamp=models.DateField("تاریخ",blank=True);
    def getMeghdar(self):
         if(self.meghdar !=  None ):
             return "{0:.0f}".format(self.meghdar)
    def getMeghdarCurrency(self):
        if(self.meghdar !=  None ):
            return format(self.meghdar,",.0f")
        return "0"
    class Meta:
        db_table="hazine"
