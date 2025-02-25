# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from djongo import models

# Model for Laptops
class CaracteristiquesLaptop(models.Model):
    Brand = models.CharField(max_length=100)
    Model_Name = models.CharField(max_length=100)
    Screen_Size = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Hard_Disk_Size = models.CharField(max_length=50)
    CPU_Model = models.CharField(max_length=50)
    Ram_Memory_Installed_Size = models.CharField(max_length=50)
    Speaker_Maximum_Output_Power = models.CharField(max_length=50)
    Connectivity_Technology = models.CharField(max_length=50)
    Audio_Output_Mode = models.CharField(max_length=50)
    Mounting_Type = models.CharField(max_length=50)
    Connector_Type = models.CharField(max_length=50)
    Compatible_Devices = models.CharField(max_length=50)
    Compatible_Phone_Models = models.CharField(max_length=50)
    Mounting_Type = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Laptop(models.Model):
    produit = models.CharField(max_length=255)
    lien = models.URLField()
    prix = models.CharField(max_length=50)
    promotion = models.CharField(max_length=10, blank=True)
    categorie = models.CharField(max_length=50)
    sous_categorie = models.CharField(max_length=50)
    site_web = models.CharField(max_length=50)
    date_extraction = models.DateTimeField()
    caracteristiques = models.EmbeddedField(
        model_container=CaracteristiquesLaptop
    )
    image_url = models.URLField()
    disponibilite = models.CharField(max_length=50)
    delai_de_livraison = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'laptop'
        
    def __str__(self):
        return self.produit


# Model for Smartphones
class CaracteristiquesSmartphone(models.Model):
    Product_Dimensions = models.CharField(max_length=100)
    Item_Weight = models.CharField(max_length=50)
    ASIN = models.CharField(max_length=50)
    Item_model_number = models.CharField(max_length=50)
    Batteries = models.CharField(max_length=100)
    Customer_Reviews = models.TextField(blank=True)
    Best_Sellers_Rank = models.TextField(blank=True)
    OS = models.CharField(max_length=50)
    Wireless_communication_technologies = models.CharField(max_length=50, blank=True)  
    Connectivity_technologies = models.CharField(max_length=100)
    GPS = models.CharField(max_length=10)
    Special_features = models.TextField(blank=True)
    Other_display_features = models.CharField(max_length=100, blank=True)
    Human_Interface_Input = models.TextField(blank=True)
    Scanner_Resolution = models.CharField(max_length=200, blank=True) 
    Other_camera_features = models.CharField(max_length=100, blank=True)
    Audio_Jack = models.CharField(max_length=50, blank=True)
    Form_Factor = models.CharField(max_length=50, blank=True)
    Color = models.CharField(max_length=50)
    Battery_Power_Rating = models.CharField(max_length=50)
    Whats_in_the_box = models.TextField(blank=True)
    Manufacturer = models.CharField(max_length=100)
    Country_of_Origin = models.CharField(max_length=100)
    Date_First_Available = models.CharField(max_length=100, blank=True)
    Memory_Storage_Capacity = models.CharField(max_length=50)
    Standing_screen_display_size = models.CharField(max_length=50)
    Ram_Memory_Installed_Size = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    Battery_Capacity = models.CharField(max_length=50, blank=True) 
    Package_Dimensions = models.CharField(max_length=50, blank=True)  
    RAM = models.CharField(max_length=50, blank=True)  
    Phone_Talk_Time = models.CharField(max_length=50, blank=True)  


    class Meta:
        abstract = True

class Smartphone(models.Model):
    produit = models.CharField(max_length=255)
    lien = models.URLField()
    prix = models.CharField(max_length=50)
    promotion = models.CharField(max_length=10, blank=True)
    categorie = models.CharField(max_length=50)
    sous_categorie = models.CharField(max_length=50)
    date_extraction = models.DateTimeField()
    caracteristiques = models.EmbeddedField(
        model_container=CaracteristiquesSmartphone
    )
    image_url = models.URLField()
    disponibilite = models.CharField(max_length=50)
    delai_de_livraison = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'smartphone'
        
    def __str__(self):
        return self.produit

