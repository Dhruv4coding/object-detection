"""
==============================================================================
Student Name: Meghraj singh | Student ID: EN19IT301048
==============================================================================
Welcome to the Real Time Object Detection Project v3 !! 

It's now detect objects live, in a web page !
Program needs Flask, OpenCV and Numpy libraries.

If you want to see older version of the program check it out my Github link!
https://github.com/mertfozzy/Real-Time-Object-Detection
  
Enjoy.
==============================================================================
"""

from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

cap = cv2.VideoCapture(0)


def gen_frames():  # frameler şeklinde görüntüleri topluyoruz
    while True:

        ret, frame = cap.read()

        # frame en boylarını aldık
        frame_width = frame.shape[1]
        frame_height = frame.shape[0]

        # görüntüyü blob formata çeviriyoruz :
        #(değişken, sabit değer, yolo416 blob ölçeği, bgr-rgb değişimi, crop)
        frame_blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)

        # modelin tanıyacağı labelları giriyoruz :
        # önceden indirdiğimiz yolo algoritmasında 80 model var :
        labels = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
                  "trafficlight", "firehydrant", "stopsign", "parkingmeter", "bench", "bird", "cat",
                  "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
                  "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sportsball",
                  "kite", "baseballbat", "baseballglove", "skateboard", "surfboard", "tennisracket",
                  "bottle", "wineglass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                  "sandwich", "orange", "broccoli", "carrot", "hotdog", "pizza", "donut", "cake", "chair",
                  "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
                  "remote", "keyboard", "cellphone", "microwave", "oven", "toaster", "sink", "refrigerator",
                  "book", "clock", "vase", "scissors", "teddybear", "hairdrier", "toothbrush"]
        
        # kutucuk renkleri ayarlıyoruz :
        # buradaki kodları teker teker konsola yazınca değer oluşuyor
        colors = ["0,255,255", "0,0,255", "255,0,0", "255,255,0", "0,255,0"]
        colors = [np.array(color.split(",")).astype("int") for color in colors]
        colors = np.array(colors)
        colors = np.tile(colors, (18, 1))
        
        # modeli import ediyoruz : algoritma başlangıcı
        model = cv2.dnn.readNetFromDarknet("C:/Users/meghr/Downloads/sused/Live-Stream-Object-Detection-main/yolov3.cfg")
        model = cv2.dnn.readNetFromDarknet("C:/Users/meghr/Downloads/sused/Live-Stream-Object-Detection-main/yolov3.weights")
        layers = model.getLayerNames()

        #çıktı katmanlarını araştırıyoruz
        output_layer = [layers[layer[0] - 1] for layer in model.getUnconnectedOutLayers()]

        model.setInput(frame_blob)

        # çıktı katmanlarını detectiona sokuyoruz
        detection_layers = model.forward(output_layer)
        # çıktı katmanlarının içindeki değerleri almış olduk.

        # ================================ non-maximum supression : operation 1 ================================
        # hatalı kutuları ve oranları yok etmek için kullanılan bir yöntemdir :
        
        ids_list = []
        boxes_list = []
        confidences_list = []

        # ================================ non-maximum supression : operation 1 end =============================

        # deteksiyona başlıyoruz. for içinde for yaparak değerler oluşturduk
        for detection_layer in detection_layers:
            for object_detection in detection_layer:

                scores = object_detection[5:] # puan tutuyoruz, 5 değer aldık
                predicted_id = np.argmax(scores) # en yüksek değerli indeksi çekiyoruz
                confidence = scores[predicted_id] # en güvenilir skoru alıyoruyz ve tutuyoruz

                if confidence > 0.35: # güvenilir skor yüzde 30dan iyiyse bounding box çizeceğiz
                    
                    # kutuyu çizerken sol alt köşeden başlayıp sağ üst köşeye gideceğiz
                    label = labels[predicted_id]
                    bounding_box = object_detection[0:4] * np.array([frame_width, frame_height, frame_width, frame_height])
                    (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")

                    # x ve y noktalarının özel koordinatı
                    start_x = int(box_center_x - (box_width / 2))
                    start_y = int(box_center_y - (box_height / 2))

                    #==================== non-maximum supression : operation 2 ====================
                    # döngü içindeki değerleri listeliyoruz ve alta iletiyoruz
                    # for içinde yukarda oluşturulan kutuları dolduruyoruz :
                    ids_list.append(predicted_id)
                    confidences_list.append(float(confidence))
                    boxes_list.append([start_x, start_y, int(box_width), int(box_height)])

                    #==================== non-maximum supression : operation 2 end ====================
        
        #============================ non-maximum supression : operation 3 =================================
        # (yukardan gelen değerlerle) max_ids içerisinde en güvenilir kutuları saklıyorum
        # cv2.dnn.NMSBoxes() maximum confidenceları liste yapar
        # 0.5 ve 0.4 trashold değerleri yani standart
        max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)

        for max_id in max_ids: # liste içindeki değeri çekeceğiz
            max_class_id = max_id[0] # max_class_id aslında nesnenin tutulduğu id olacak
            box = boxes_list[max_class_id] # box en iyi değeri tutacak

            start_x = box[0] # box'un başlangıç noktası indis değeri
            start_y = box[1]
            box_width = box[2]
            box_height = box[3] # box eni ve boyu

            predicted_id = ids_list[max_class_id] # label yazmak için max_classı kullandık
            label = labels[predicted_id] # ilgili labelı yukardan uygun şekilde çektik
            confidence = confidences_list[max_class_id] # confidence oranı sağlam olanı aldık

        #============================ non-maximum supression : operation 3 end =================================

        end_x = start_x + box_width
        end_y = start_y + box_height

        box_color = colors[predicted_id]
        box_color = [int(each) for each in box_color]
        label = "{}: {:.2f}%".format(label, confidence * 100)
        print("predicted object {}".format(label))

        # kutuyla ilgili tüm parametreler hazır. çizim başlıyor :
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), box_color, 2)
        cv2.putText(frame, label, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #outputu stream ediyoruz :
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Real Time Object Detection v3."""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
