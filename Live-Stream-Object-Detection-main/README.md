![photo](https://github.com/mertfozzy/Live-Stream-Object-Detection/blob/main/photo.png?raw=true)
# Live-Stream-Object-Detection

---------------------------------------------------T U R K I S H------------------------------------------------------------------

Proje Sahibi: Mert Altuntaş

Proje Tanımı: Bu projenin amacı, nesneleri gerçek zamanlı olarak iyi bir doğrulukla tespit etmektir. Nesneler, web kamerasında canlı olarak kare veya daire içine alınmış bir alanda görünecektir. Uygulama bir web aplikasyonudur.

Tüm kodlar Mert Altuntaş tarafından yazılmıştır.

Yazılımlar ve Kütüphaneler:
Bu proje için gerekli yazılımlar;
- Programlama dili olarak Python 3.7 (veya üstü)
- Python kütüphanelerini kullanmak için Anaconda Dağıtımları
- Geliştirme ortamı olarak Pycharm Pro, Spyder veya Visual Studio Code
- Web geliştirme için Flask kütüphanesi
- Nesneleri algılamak için OpenCV kütüphanesi
- Matrisler oluşturmak ve hesaplamalar yapmak için Numpy kütüphanesi
- Proje dosyalarını saklamak ve proje sürümlerini izlemek için Github Öğrenci Geliştirici Paketi.


Gerekli Araçlar:
- Windows 10 veya Linux tabanlı bilgisayar
- Web Kamerası veya Ek Kamera
- XAMPP Control Panel v3.3.0


İşlevsel gereksinimler :
- Öncelikle program bir masaüstü uygulaması olacak.
- Program, bir web kamerasındaki nesneleri algılayacaktır. Kullanıcılar nesneleri kare içine alınmış bir alanda görebilir.
- Program ayrıca gerçek zamanlı olarak çalışmalıdır. Tüm tespitler canlı olmalı.
- Ayrıca program 80'e yakın farklı nesneyi algılayabilecektir. Veri setim YOLOv3'e dayalı olacaktır.


Eski versiyon için : https://github.com/mertfozzy/Real-Time-Object-Detection


Nasıl Çalışır ?
- https://pjreddie.com/darknet/yolo/ adresinden yolov3-416 paketini indirin. Kodda belirtilen adreslere bu dosyaları kaydedin.
- Projemizi oluşturalım ; indirdiğimiz dosyayı ve kütüphaneleri dahil edin. (opencv-numpy-flask)
- Anaconda dağıtımından yararlanacaksak conda konsolundan kütüphane indirebilirsiniz. Pycharm üzerinde kütüphaneler kurulabilir.
- XAMPP Control Panel üzerinden Apache ve MySQL sunucularını aktif edin.
- Python Interpreter'inizi seçip kodu derleyin. Ardından, tarayıcınız üzerinden localhost:5000 adresine gidin.
- Deteksiyon penceresi ile karşılaşacaksınız. Objeleriniz web sayfası üzerinden algılanacaktır.
- Bu aşamada görüntü donanıma bağlı olarak yavaş olabilir. Programdan çıkış yapmak için tarayıcıyı kapamanız yeterlidir.


-----------------------------------------------------E N G L I S H----------------------------------------------------------------

Project Owner : Mert Altuntaş

Project Description : The aim of this project is to detect the objects in real time with good accuracy. Objects will appear live on webcam in a squared or circled area. This project is a web application.

All the datas and codes created by Mert Altuntaş.

Tools and Frameworks :
For this project required softwares are ;
-	Python 3.7 (or above) as programming language
-	Anaconda Distributions to use Python libraries
-	Pycharm Pro, Spyder or VS Code as a developing environments
-	Flask library for web development
-	OpenCV Libraries to detect objects
-	Numpy Libraries to create matrices and making calculations
-	Github Student Developer Pack for keeping project files and tracking project versions.


Required Equipment :
-	Windows 10 or Linux based computer
-	Webcam or Additional Camera
-	XAMPP Control Panel v3.3.0


Functional Requirements :
- First of all, the program is a desktop application. 
- The program will detect objects from a webcam. Users can see the objects in a squared or circled area.
- The program also should work in real time. All detections have to be live.
- Also, the program will be able to detect almost 80 different objects. My dataset will be based on YOLOv3.


For older version : https://github.com/mertfozzy/Real-Time-Object-Detection

How does it work ?
- Download yolov3-416 package from this address : https://pjreddie.com/darknet/yolo/. Save these files to the addresses specified in the code.
- Let's create our project; Include the file and libraries we downloaded. (opencv-numpy)
- If you are going to use Anaconda distribution, you can download the library from the conda console. Libraries can be installed on PyCharm.
- Activate Apache and MySQL servers via XAMPP Control Panel.
- Select your Python Interpreter and compile the code. Next, navigate to localhost: 5000 through your browser.
- You will see the detection window. Your objects will be detected on the web page.
- At this stage, the image may be slow depending on the hardware. To exit the program, simply close the browser.
