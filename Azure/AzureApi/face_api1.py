import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

KEY = '37323a30ac92479eb7135fa97acf1075'

ENDPOINT = 'https://openvisiondemo.cognitiveservices.azure.com/'

url_base = 'eastus.api.cognitive.microsoft.com'



class FaceID:
	def __init__(self, key = KEY):
		self.key = key

	def detectFace(self, url): # returns faceId
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		    # Request parameters
		    'returnFaceId': 'true',
		    'returnFaceLandmarks': 'false',
		    'recognitionModel': 'recognition_04',
		    'returnRecognitionModel': 'false',
		    'detectionModel': 'detection_03',
		    'faceIdTimeToLive': '86400',
		})

		body = json.dumps({'url': url})
		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    data = json.loads(data)
		    id = ''
		    mx = 0
		    for x in data:
		    	if x['faceRectangle']['width'] > mx:
		    		mx = x['faceRectangle']['width']
		    		id = x['faceId']
		    conn.close()
            
		except Exception as e:
			print("[Errno {0}] {1}".format(e.errno, e.strerror))
            
		return id
    

	def createGroup(self, personGroupId, groupName, groupData = ""):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-key': self.key,
		}

		body = json.dumps({
		    "name": groupName,
		    "userData": groupData,
		    "recognitionModel": "recognition_04"
		})
		params = urllib.parse.urlencode({
		})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("PUT", f"/face/v1.0/persongroups/{personGroupId}?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    print(data)
		    conn.close()
            
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))


	def deleteGroup(self, personGroupId):
		headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("DELETE", f"/face/v1.0/persongroups/{personGroupId}?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    print(data)
		    conn.close()
            
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))


	def addPersonToGroup(self, personGroupId, personName, userData = ''):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({
		    "name": personName,
		    "userData": userData
		})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("POST", f"/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    data = json.loads(data)
		    print(data)
		    conn.close()
            
		    return data['personId']
        
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))


	def deletePersonFromGroup(self, personGroupId, personId):
		headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("DELETE", f"/face/v1.0/persongroups/{personGroupId}/persons/{personId}?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    print(data)
		    conn.close()
            
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
            

	def addFaceToPerson(self, personGroupId, personId, url, userData = ''):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		    # Request parameters
		    'userData': userData,
		    'targetFace': '',
		    'detectionModel': 'detection_03',
		})

		body = json.dumps({'url': url})
		
		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("POST", f"/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    print(data)
		    conn.close()
            
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))


	def trainGroup(self, personGroupId):
		headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("POST", f"/face/v1.0/persongroups/{personGroupId}/train?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    print(data)
		    conn.close()
            
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))


	def isTrained(self, personGroupId):
		headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("GET", f"/face/v1.0/persongroups/{personGroupId}/training?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    conn.close()
            
		    data = json.loads(data)
		    if 'error' in data:
		    	return False
            
		    return (data['status'] == 'succeeded')
        
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
            

	def identifyFace(self, url, personGroupId):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': self.key,
		}

		params = urllib.parse.urlencode({
		})

		body = json.dumps({
		    "personGroupId": personGroupId,
		    "faceIds": [
		    	self.detectFace(url)
		    ],
		    "maxNumOfCandidatesReturned": 1,
		})

		try:
		    conn = http.client.HTTPSConnection(url_base)
		    conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
		    response = conn.getresponse()
		    data = response.read().decode('utf-8')
		    data = json.loads(data)
		    print(data)
		    conn.close()
            
		    if 'error' in data:
		    	return 0
            
		    return (data[0]['candidates'][0]['personId'])
        
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
            

#F = FaceID()
		    
#F.createGroup('01', "test")
#eminemId = F.addPersonToGroup('01', "Eminem")
#F.addFaceToPerson('01', eminemId, 'https://n1s1.starhit.ru/a6/1b/20/a61b202ca030fe9528a97eb55b5c1c4a/444x460_0_7056e5e0550c48c8d1a6434634ea754f@480x497_0xac120003_12391102121602250828.jpg')
#F.trainGroup("01")
#print(F.isTrained("01"))

#print(F.identifyFace('https://www.biography.com/.image/t_share/MTQ3NjM5MTEzMTc5MjEwODI2/eminem_photo_by_dave_j_hogan_getty_images_entertainment_getty_187596325.jpg', "01"))