#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
# uvicorn Filtro_Query:app --reload

#Definimos nuestra entidad: Celular
class Celular(BaseModel):
    id:int
    marca:str
    modelo:str
    procesador:str
    sistema:str
    ram:str
    interna:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
celulares_list= [
    
Celular(id=1, marca="Samsung", modelo="Galaxy A34", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=2, marca="Motorola", modelo="Edge 20 Lite", procesador="MediaTek Dimensity 720", sistema="Android 11", ram="6GB", interna="128GB"), 

Celular(id=3, marca="Xiaomi", modelo="Redmi Note 12", procesador="Qualcomm SM4375 Snapdragon", sistema="Android 12", ram="4GB", interna="128GB"), 

Celular(id=4, marca="Apple", modelo="14 Pro Max", procesador="Apple A16 Bionic", sistema="iOS", ram="6GB", interna="256GB"), 

Celular(id=5, marca="Samsung", modelo="S23 Ultra", procesador="Qualcomm Snapdragon SM8550", sistema="Android", ram="12GB", interna="256GB"), 

Celular(id=6, marca="Samsung", modelo="Galaxy S10e", procesador="Qualcomm Snapdragon 855", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=7, marca="Motorola", modelo="Moto G42", procesador="8 núcleos", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=8, marca="Xiaomi", modelo="Redmi Note 12S", procesador="MediaTek Helio G96", sistema="Android 13", ram="8GB", interna="256GB"), 

Celular(id=9, marca="Apple", modelo="11", procesador="Apple A13 Bionic", sistema="iOS", ram="4GB", interna="128GB"), 

Celular(id=10, marca="Samsung", modelo="Galaxy Z Flip 4", procesador="Octa Core", sistema="Android 13", ram="8GB", interna="256GB"), 

Celular(id=11, marca="Xiaomi", modelo="Redmi A2", procesador="MediaTek Helio G35", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=12, marca="Hisense", modelo="Hisense E20", procesador="8 núcleos", sistema="Android 10", ram="2GB", interna="256GB"), 

Celular(id=13, marca="Huawei", modelo="Mate 50 Pro", procesador="Snapdragon 865+", sistema="EMUI 13", ram="8GB", interna="256GB"), 

Celular(id=14, marca="Nokia", modelo="C20", procesador="8 núcleos", sistema="Android 10", ram="2GB", interna="32GB"), 

Celular(id=15, marca="Apple", modelo="XS", procesador="Apple A12", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=16, marca="Samsung", modelo="Galaxy A04E", procesador="MediaTek Helio P35", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=17, marca="Motorola", modelo="Moto G82 5G", procesador="Qualcomm Snapdragon 695 5G", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=18, marca="Huawei", modelo="Nova Y61", procesador="Octa Core", sistema="EMUI 12", ram="4GB", interna="64GB"), 

Celular(id=19, marca="Huawei", modelo="Nova 11i", procesador="Qualcomm Snapdragon 680", sistema="EMUI 13", ram="8GB", interna="128GB"), 

Celular(id=20, marca="Xiaomi", modelo="Redmi A1", procesador="8 núcleos", sistema="Android 12", ram="2GB", interna="32GB"), 

Celular(id=21, marca="Samsung", modelo="Galaxy S21+", procesador="8 núcleos", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=22, marca="Motorola", modelo="g52", procesador="Octa-Core Qualcomm", sistema="Android", ram="6GB", interna="256GB"), 

Celular(id=23, marca="Samsung", modelo="Galaxy A14", procesador="Exynos 1200", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=24, marca="Xiaomi", modelo="Poco X5", procesador="Snapdragon 695", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=25, marca="Apple", modelo="iPhone 13", procesador="Chip a15 bionic", sistema="iOS", ram="4GB", interna="128GB"), 

Celular(id=26, marca="Samsung", modelo="Galaxy A53 5G", procesador="Samsung Exynos 1280", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=27, marca="Apple", modelo="iPhone 12", procesador="A14 Bionic", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=28, marca="Huawei", modelo="P60 Pro", procesador="Qualcomm snapdragon 8+ gen1", sistema="EMUI 13.1", ram="8GB", interna="256GB"), 

Celular(id=29, marca="Xiaomi", modelo="Redmi Note 11", procesador="Mediatek Dimensity 810", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=30, marca="Motorola", modelo="Moto G41", procesador="Mediatek Helio G85", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=31, marca="Xiaomi", modelo="Redmi A2", procesador="MediaTek Helio G37", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=32, marca="Apple", modelo="XR", procesador="Apple A12", sistema="iOS", ram="3GB", interna="64GB"), 

Celular(id=33, marca="Samsung", modelo="Galaxy A53", procesador="Octa Core", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=34, marca="Samsung", modelo="Galaxy S22 Ultra", procesador="Snapdragon", sistema="Android", ram="12GB", interna="256GB"), 

Celular(id=35, marca="Motorola", modelo="Moto G60", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=36, marca="Motorola", modelo="Moto G31", procesador="MediaTek Helio G85", sistema="Android", ram="8GB", interna="64GB"), 

Celular(id=37, marca="Apple", modelo="iPhone X", procesador="iOS", sistema="iOS", ram="3GB", interna="64GB"), 

Celular(id=38, marca="Apple", modelo="iPhone 13 Pro Max", procesador="Apple A14", sistema="iOS", ram="6GB", interna="128GB"), 

Celular(id=39, marca="Honor", modelo="X7A", procesador="MediaTek Helio G37", sistema="Android 12", ram="6GB", interna="128GB"), 

Celular(id=40, marca="Samsung", modelo="Galaxy A33", procesador="Exynos 1280", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=41, marca="Honor", modelo="Honor X6", procesador="Mediatek helio", sistema="Android 12", ram="4GB", interna="64GB"), 

Celular(id=42, marca="Honor", modelo="Honor X8A", procesador="8 núcleos", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=43, marca="Apple", modelo="iPhone 12 Pro", procesador="Chip A14 Bionic ", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=44, marca="Motorola", modelo="Motorola G13", procesador="8 núcleos", sistema="Android 13", ram="4GB", interna="128GB"), 

Celular(id=45, marca="Xiaomi", modelo="Redmi 9A", procesador="MediaTek Helio G25", sistema="Android 11", ram="4GB", interna="64GB"), 

Celular(id=46, marca="Xiaomi", modelo="Redmi Note 10S", procesador="MediaTek Helio G95", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=47, marca="Motorola", modelo="Moto e13", procesador="8 núcleos", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=48, marca="Xiaomi", modelo="Redmi Note 11S", procesador="MediaTek Helio G96", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=49, marca="Samsung", modelo="Galaxy S22 Ultra 5G", procesador="Samsung Exynos 2200", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=50, marca="Motorola", modelo="Moto G41", procesador="Helio G85", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=51, marca="Xiaomi", modelo="Redmi K50 Gaming", procesador="Snapdragon 8", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=52, marca="Apple", modelo="iPhone 11 Pro", procesador="Apple A13", sistema="iOS", ram="4GB", interna="128GB"), 

Celular(id=53, marca="Samsung", modelo="Galaxy A03 Core", procesador="Unisistemac SC9863A", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=54, marca="Xiaomi", modelo="Redimi 9T", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=55, marca="Samsung", modelo="Galaxy A03 Core", procesador="Unisistemac SC9863A", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=56, marca="Xiaomi", modelo="Redmi Note 11S 5G", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=57, marca="Xiaomi", modelo="Redmi A2", procesador="Octa Core", sistema="Android", ram="16GB", interna="64GB"), 

Celular(id=58, marca="Huawei", modelo="Nova 11l", procesador="Octa Core", sistema="EMUI 11", ram="8GB", interna="128GB"), 

Celular(id=59, marca="Oppo", modelo="Reno 7", procesador="Octa Core", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=60, marca="Motorola", modelo="Moto G13", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=61, marca="Huawei", modelo="Y7A", procesador="Octa Core", sistema="EMUI 10", ram="8GB", interna="128GB"), 

Celular(id=62, marca="Honor", modelo="9x", procesador="Octa Core", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=63, marca="OnePlus", modelo="N10", procesador="Octa Core", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=64, marca="Motorola", modelo="G72", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=65, marca="Oppo", modelo="A77", procesador="Octa Core", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=66, marca="Honor", modelo="X7A", procesador="Octa Core", sistema="Android", ram="16GB", interna="128GB"), 

Celular(id=67, marca="Huawei", modelo="Nova 10 SE", procesador="Octa Core", sistema="EMUI 11", ram="8GB", interna="128GB"), 

Celular(id=68, marca="Zuum", modelo="Magno C2", procesador="Quad Core", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=69, marca="Huawei", modelo="Y9 2018", procesador="Octa Core", sistema="EMUI 10", ram="8GB", interna="128GB"), 

Celular(id=70, marca="Huawei", modelo="Y8s", procesador="HiSilicon Kirin", sistema="EMUI 10", ram="8GB", interna="128GB"), 

Celular(id=71, marca="Huawei", modelo="P30 Lite Dual", procesador="Kirin 710 Octa core", sistema="EMUI 11", ram="8GB", interna="128GB"), 

Celular(id=72, marca="Samsung", modelo="M12", procesador="Exynos 850", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=73, marca="Samsung", modelo="Galaxy A04", procesador="Unisistemac SC9863A Octa core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=74, marca="Samsung", modelo="Galaxy S22 Ultra", procesador="Exynos 2200 a 28GHz", sistema="Android", ram="16GB", interna="128GB"), 

Celular(id=75, marca="Samsung", modelo="Galaxy A13", procesador="Exynos 850", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=76, marca="Samsung", modelo="Galaxy S22 Ultra", procesador="Dynamic AMOLED 2X", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=77, marca="Samsung", modelo="Galaxy A03s", procesador="Qualcomm SDM450", sistema="Android", ram="16GB", interna="64GB"), 

Celular(id=78, marca="Samsung", modelo="Galaxy A33", procesador="Exynos 1280", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=79, marca="Samsung", modelo="Galaxy A22", procesador="MediaTek MT6769T Helio G80 Octa Core", sistema="Android", ram="8GB", interna="256GB"),

Celular(id=80, marca="Samsung", modelo="Galaxy Z Flip4", procesador="Snapdragon 8 + Gen 1 4nm", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=81, marca="Motorola", modelo="G50", procesador="Snapdragon 662", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=82, marca="Motorola", modelo="Edge 30 Neo", procesador="Qualcomm SD3675", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=83, marca="Motorola", modelo="Moto E7 PLUS", procesador="Snapdragon 460", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=84, marca="Motorola", modelo="Edge 30", procesador="Qualcomm Snapdragon", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=85, marca="Motorola", modelo="G42", procesador="Qualcomm Snapdragon 680 ocho núcleos", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=86, marca="Xiaomi", modelo="Redmi A1", procesador="Mediatek MT6761/4 CUADCORE", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=87, marca="Samsung", modelo="Galaxy A04E", procesador="Exynos 1280", sistema="Android", ram="8 GB", interna="128GB"), 

Celular(id=88, marca="Motorola", modelo="G42", procesador="Snapdragon 680", sistema="Android", ram="16GB", interna="64GB"), 

Celular(id=89, marca="ZTE", modelo="Blade L9", procesador="Quad Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=90, marca="Zuum", modelo="Magno C2", procesador="Quad Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=91, marca="Motorola", modelo="E20", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=92, marca="Zuum", modelo="Rocket III", procesador="Quad Core", sistema="Android", ram="8 GB", interna="256GB"), 

Celular(id=93, marca="Bmobile", modelo="AX751", procesador="Quad Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=94, marca="Lanix", modelo="X1", procesador="Quad Core", sistema="Android", ram="16GB", interna="512GB"), 

Celular(id=95, marca="Zuum", modelo="Stellar M4", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=96, marca="Zuum", modelo="Akus P1", procesador="Octa Core de 1.5 GHz", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=97, marca="Bmobile", modelo="AX751", procesador="Quad Core", sistema="Android", ram="16GB", interna="512GB"), 

Celular(id=98, marca="ZTE", modelo="Blade A31", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=99, marca="Zuum", modelo="Hidra X", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=100, marca="ZTE", modelo="Blade V40 Smart", procesador="Octa Core", sistema="Android 11", ram="3GB", interna="64GB"),

Celular(id=101, marca="Samsung", modelo="Galaxy A54 5G", procesador="Samsung exynos 1280", sistema="Android", ram="8GB", interna="256GB"),

Celular(id=102, marca="Apple", modelo="13 Mini", procesador="Chip a15 bionic", sistema="iOS", ram="4GB", interna="128GB"),

Celular(id=103, marca="Apple", modelo="iPhone 14 Pro", procesador="Apple A16 Bionic", sistema="iOS", ram="8GB", interna="256GB"),

Celular(id=104, marca="Samsung", modelo="S23 Ultra", procesador="Qualcomm Snapdragon SM8550", sistema="Android", ram="8GB", interna="256GB"),

Celular(id=105, marca="Samsung", modelo="Galaxy Z Flip5", procesador="Qualcomm Snapdragon SM8550", sistema="Android", ram="12GB", interna="256GB"),

Celular(id=106, marca="Hisense", modelo="Hisemse E50", procesador="Spreadtrum Unisistemac SC9832E", sistema="Android 11", ram="4GB", interna="256GB"), 

Celular(id=107, marca="Motorola", modelo="Edge 30 Pro o Edge+", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=108, marca="OnePlus", modelo="10 Pro", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="2GB", interna="64GB"), 

Celular(id=109, marca="Realme", modelo="GT 2 Pro", procesador="Snapdragon 8 Gen 1", sistema="Android 12", ram="12GB", interna="256GB"), 

Celular(id=110, marca="Honor", modelo="Magic V", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=111, marca="Samsung", modelo="Galaxy Z Fold 3", procesador="Qualcomm Snapdragon SM8550", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=112, marca="Samsung", modelo="Galaxy S", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=113, marca="Motorola", modelo="Moto G42", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="12GB", interna="256GB"), 

Celular(id=114, marca="Honor", modelo="Magic 4", procesador="Snapdragon 8 Gen 1", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=115, marca="Oppo", modelo="Find X5 Pro", procesador="Snapdragon 8 Gen 1", sistema="Android 10", ram="2GB", interna="32GB"), 

Celular(id=116, marca="Samsung", modelo="Galaxy Note", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=117, marca="Samsung", modelo="Galaxy A32 5G", procesador="MediaTek Dimensity 720", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=118, marca="Nokia", modelo="2.4", procesador="MediaTek Helio P22", sistema="Android 11", ram="2GB", interna="32GB"), 

Celular(id=119, marca="Xiaomi", modelo="13 Pro", procesador="Qualcomm Snapdragon 8 Gen 2", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=120, marca="OnePlus", modelo="11", procesador="Qualcomm Snapdragon 8 Gen 2", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=121, marca="Samsung", modelo="Galaxy S23 Ultra", procesador="Qualcomm Snapdragon 8 Gen 2", sistema="Android", ram="8 GB", interna="256GB"), 

Celular(id=122, marca="Apple", modelo="iPhone XR", procesador="Apple A16 Bionic", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=123, marca="Apple", modelo="iPhone 14 Pro Max", procesador="Apple A16 Bionic", sistema="iOS", ram="8GB", interna="128GB"), 

Celular(id=124, marca="Samsung", modelo="Galaxy a55", procesador="Exynos 2200", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=125, marca="Samsung", modelo="Galaxy S22", procesador="Exynos 2200", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=126, marca="Xiaomi", modelo="Redmi A1", procesador="8 núcleos", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=127, marca="Google", modelo="Pixel 7", procesador="Tensistemar G2", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=128, marca="Google", modelo="Pixel 7 Pro", procesador="Tensistemar G2", sistema="Android", ram="2GB", interna="64GB"), 

Celular(id=129, marca="Huawei", modelo="Mate 40", procesador="HiSilicon Kirin 9000", sistema="EMUI 10", ram="8GB", interna="256GB"), 

Celular(id=130, marca="Huawei", modelo="Mate 40 Pro", procesador="HiSilicon Kirin 9000", sistema="EMUI 10", ram="8GB", interna="256GB"), 

Celular(id=131, marca="Vivo", modelo="X80 Pro 5G", procesador="MediaTek Dimensity 9000", sistema="Android", ram="4GB", interna="32GB"), 

Celular(id=132, marca="Honor", modelo="70 Pro", procesador="MediaTek Dimensity 9000", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=133, marca="Honor", modelo="70 Pro+", procesador="MediaTek Dimensity 9000", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=134, marca="Xiaomi", modelo="Redmi K50 Pro", procesador="MediaTek Dimensity 9000", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=135, marca="Apple", modelo="iPhone 14", procesador="Apple A14", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=136, marca="Apple", modelo="iPhone 14 Plus", procesador="Apple A14", sistema="iOS", ram="8GB", interna="128GB"), 

Celular(id=137, marca="Apple", modelo="iPhone 14 Pro", procesador="Apple A14", sistema="iOS", ram="8GB", interna="256GB"), 

Celular(id=138, marca="Apple", modelo="iPhone 14 Pro Max", procesador="Apple A14", sistema="iOS", ram="8GB", interna="256GB"), 

Celular(id=139, marca="Samsung", modelo="Galaxy S23 Ultra", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=140, marca="Xiaomi", modelo="13 Pro", procesador="Dynamic AMOLED 2X", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=141, marca="OnePlus", modelo="11", procesador="Apple A12", sistema="Android", ram="8 GB", interna="256GB"), 

Celular(id=142, marca="Google", modelo="Pixel 7 Pro", procesador="MediaTek Helio G85", sistema="Android 13", ram="8GB", interna="128GB"), 

Celular(id=143, marca="Apple", modelo="iPhone X", procesador="iOS", sistema="iOS", ram="8GB", interna="256GB"), 

Celular(id=144, marca="Apple", modelo="iPhone SE", procesador="Apple A14", sistema="iOS", ram="8GB", interna="256GB"), 

Celular(id=145, marca="Honor", modelo="X7A", procesador="MediaTek Helio G37", sistema="Android", ram="8 GB", interna="256GB"), 

Celular(id=146, marca="Samsung", modelo="Galaxy S", procesador="Exynos", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=147, marca="Samsung", modelo="Galaxy SII", procesador="SistemaC Exynos 4210", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=148, marca="Samsung", modelo="Galaxy Note 20", procesador="Exynos 990", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=149, marca="Apple", modelo="iPhone 8", procesador="iOS", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=150, marca="Motorola", modelo="Moto G100", procesador="Snapdragon 870", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=151, marca="Xiaomi", modelo="Redmi Note 10 Pro", procesador="Snapdragon 732G", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=152, marca="Samsung", modelo="Galaxy S20 FE", procesador="Snapdragon 865", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=153, marca="Vivo", modelo="V20", procesador="Snapdragon 720G", sistema="Android 11", ram="8GB", interna="128GB"), 

Celular(id=154, marca="Xiaomi", modelo="Redmi 9A", procesador="MediaTek Helio G25", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=155, marca="Xiaomi", modelo="Redmi Note 10S", procesador="MediaTek Helio G95", sistema="Android", ram="4GB", interna="64GB"),

Celular(id=156, marca="Motorola", modelo="Moto e13", procesador="8 núcleos", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=157, marca="Xiaomi", modelo="Redmi Note 11S", procesador="MediaTek Helio G96", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=158, marca="Samsung", modelo="Galaxy A14", procesador="Samsung Exynos 2200", sistema="Android", ram="4GB", interna="64GB"), 

Celular(id=159, marca="Motorola", modelo="Moto G41", procesador="Helio G85", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=160, marca="Xiaomi", modelo="Redmi K50 Gaming", procesador="Snapdragon 8", sistema="Android 12", ram="12GB", interna="256GB"), 

Celular(id=161, marca="Apple", modelo="SE2", procesador="Apple A13", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=162, marca="Samsung", modelo="A04e", procesador="Unisistemac SC9863A", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=163, marca="Xiaomi", modelo="Redmi 9T", procesador="Octa Core", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=164, marca="Samsung", modelo="Galaxy A03 Core", procesador="Unisistemac SC9863A", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=165, marca="Xiaomi", modelo="Redmi Note 11S", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=166, marca="Xiaomi", modelo="Redmi A2", procesador="Octa Core", sistema="Android", ram="2GB", interna="32GB"), 

Celular(id=167, marca="Huawei", modelo="Nova 11l", procesador="Octa Core", sistema="EMUI 12", ram="6GB", interna="128GB"), 

Celular(id=168, marca="Honor", modelo="90 Lite", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=169, marca="itel", modelo="Vision 2S", procesador="Octa Core", sistema="Android 11", ram="2GB", interna="32GB"), 

Celular(id=170, marca="itel", modelo="Vision 3 Turbo", procesador="Octa Core", sistema="Android 11", ram="3GB", interna="64GB"), 

Celular(id=171, marca="itel", modelo="A23S", procesador="Quad-core 1.4 GHz", sistema="Android 11", ram="2GB", interna="32GB"), 

Celular(id=172, marca="OnePlus", modelo="N10", procesador="Octa Core", sistema="Android 11", ram="8GB", interna="128GB"), 

Celular(id=173, marca="Motorola", modelo="G72", procesador="Octa Core", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=174, marca="Oppo", modelo="A54", procesador="Octa Core", sistema="Android 10", ram="4GB", interna="128GB"), 

Celular(id=175, marca="Honor", modelo="X7A", procesador="Octa Core", sistema="Android 12", ram="6GB", interna="128GB"), 

Celular(id=176, marca="Motorola", modelo="G41", procesador="Octa Core", sistema="Android 11", ram="4GB", interna="128GB"), 

Celular(id=177, marca="Vivo", modelo="Y100", procesador="Mediatek MT6877", sistema="Android 13", ram="8GB", interna="128GB"), 

Celular(id=178, marca="Asus", modelo="ROG Phone 7 Ultimate", procesador="Octa Core", sistema="Android 13", ram="16GB", interna="512GB"), 

Celular(id=179, marca="Google", modelo="Pixel 6a", procesador="8 núcleos", sistema="Android 12", ram="8GB", interna="256GB"), 

Celular(id=180, marca="Huawei", modelo="P30 Lite", procesador="Kirin 710 Octa core", sistema="EMUI 12", ram="8GB", interna="256GB"), 

Celular(id=181, marca="Huawei", modelo="Nova 10 Pro", procesador="Qualcomm snapdragon 778g", sistema="EMUI 12", ram="8GB", interna="256GB"), 

Celular(id=182, marca="Samsung", modelo="Galaxy A04", procesador="Unisoc SC9863A ", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=183, marca="Samsung", modelo="Galaxy A03", procesador="Unisoc T606", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=184, marca="Motorola", modelo="Moto G60S", procesador="8 núcleos", sistema="Android 11", ram="6GB", interna="128GB"), 

Celular(id=185, marca="Samsung", modelo="Galaxy S22 Ultra", procesador="Dynamic AMOLED 2X", sistema="Android", ram="12GB", interna="256GB"), 

Celular(id=186, marca="Honor", modelo="X5", procesador="Octa Core", sistema="Android 12", ram="2GB", interna="32GB"), 

Celular(id=187, marca="Samsung", modelo="Galaxy A33", procesador="Exynos 1280", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=188, marca="Oppo", modelo="Reno 6 5G", procesador="MediaTek Dimensity 900", sistema="Android", ram="8GB", interna="128GB"),

Celular(id=189, marca="Samsung", modelo="M33", procesador="Snapdragon 8 + Gen 1 4nm", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=190, marca="Motorola", modelo="G50", procesador="Snapdragon 662", sistema="Android", ram="4GB", interna="128GB"), 

Celular(id=191, marca="Xiaomi", modelo="11T Pro", procesador="Snapdragon 888", sistema="Android", ram="8GB", interna="256GB"), 

Celular(id=192, marca="Apple", modelo="iPhone 11 Pro Max", procesador="A13 Bionic", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=193, marca="Apple", modelo="iPhone 11", procesador="A13 Bionic", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=194, marca="Apple", modelo="iPhone 11 Pro", procesador="A13 Bionic", sistema="iOS", ram="4GB", interna="64GB"), 

Celular(id=195, marca="Samsung", modelo="Galaxy S21+", procesador="Exynos 2100", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=196, marca="Samsung", modelo="Galaxy S21", procesador="Exynos 2100", sistema="Android", ram="6GB", interna="128GB"), 

Celular(id=197, marca="Samsung", modelo="Galaxy A54 5G", procesador="Octa Core", sistema="Android", ram="8GB", interna="128GB"), 

Celular(id=198, marca="Apple", modelo="iPhone 13", procesador="A15 Bionic", sistema="iOS", ram="4GB", interna="512GB"), 

Celular(id=199, marca="Apple", modelo="iPhone 13 mini", procesador="A15 Bionic", sistema="iOS", ram="4GB", interna="128GB"), 

Celular(id=200, marca="Apple", modelo="iPhone 13 Pro Max", procesador="A15 Bionic", sistema="iOS", ram="6GB", interna="128GB")
                
             ]


#***Get con Filtro Query para ID
@app.get("/celularesclass/")
async def celularesclass(id:int):
    celulares=filter (lambda celular: celular.id == id, celulares_list)  #Función de orden superior
    try:
        return list(celulares)[0]
    except:
        return{"error":"No se ha encontrado el celular"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
 #***Get con Filtro Query
# @app.get("/celularesclass2/")
# async def celularesclass(marca: str, procesador: str):
#     celulares = filter (lambda celular: celular.marca == marca, celulares_list)
#     celulares1 = filter (lambda celular: celular.procesador == procesador, celulares_list)#Función de orden superior
#     try:
#         return list(celulares1)[0]
#     except IndexError:
#         return{"error":"No se ha encontrado el celular"}

#Ruta que filtra elementos por marca y procesador 2 criterios
@app.get("/celulares/")
async def get_celulares(marca: str, procesador: str):
    filtrar_celulares = filter (lambda celular: celular.marca == marca and 
                             celular.procesador == procesador, celulares_list)
    return list(filtrar_celulares)

#Ruta que filtra elementos por marca, procesador y sistema operativo 3 criterios
@app.get("/celularesclass3/")
async def get_celulares(marca: str, procesador: str, sistema: str):
    filtrar_celulares = filter (lambda celular: celular.marca == marca and 
                             celular.procesador == procesador
                             and celular.sistema == sistema, celulares_list)
    return list(filtrar_celulares)

#Ruta que filtra elementos por marca, procesador, sistema operativo y memoria RAM 4 criterios
@app.get("/celularesclass4/")
async def get_celulares(marca: str, procesador: str, sistema: str, ram: str):
    filtrar_celulares = filter (lambda celular: celular.marca == marca and 
                             celular.procesador == procesador
                             and celular.sistema == sistema and celular.ram == ram, celulares_list)
    return list(filtrar_celulares)

#Ruta que filtra elementos por marca, procesador, sistema operativo, memoria RAM y memoria interna 5 criterios
@app.get("/celularesclass5/")
async def get_celulares(marca: str, procesador: str, sistema: str, ram: str, interna:str):
    filtrar_celulares = filter (lambda celular: celular.marca == marca and 
                             celular.procesador == procesador
                             and celular.sistema == sistema and celular.ram == ram
                             and celular.interna == interna, celulares_list)
    return list(filtrar_celulares)


 
