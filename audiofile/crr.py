import re
#import logging
import time
import os
from random import randint
from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import *
from werkzeug.utils import secure_filename
import requests
import json

app=Flask(__name__,instance_relative_config=True)




app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'F:/Program Files/Microsoft SQL Server/MSSQL15.MSSQLSERVER/MSSQL'))

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_DATABASE_URI']="mssql+pyodbc://DESKTOP-URHHJQ5/atm6?driver=SQL+Server?trusted_connection=yes"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)



class song(db.Model) :
    id = db.Column( db.Integer,primary_key=True)
    Name_of_song = db.Column(db.String(100),nullable=False,unique=True)
    duration_time=db.Column(db.Integer,default=0,nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)


#class AudioBook(db.Model):
    #title = Column(db.String(100), nullable=False)
    #author = Column(db.String(100), nullable=False)
    #narrator = Column(db.String(100), nullable=False)
    #uploaded_time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    #duration_time=db.Column(db.Integer,default=0,nullable=False)


#class Podcast(db.Model):
    #name = Column(db.String(100), nullable=False)
    #host = Column(db.String(100), nullable=False)
    #participents = Column(db.Text, nullable=False)
    #uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #duration_time=db.Column(db.Integer,default=0,nullable=False)
 



audiofiletype = {"song": song}
#audiofiletype = {"song": song, "audiobook": audioBook, "podcast": podcast}

'''@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'''



@app.route('/',methods=['POST','GET'])
def menu():
    ''' accessing the credentials'''
    #return 'server is runnng'
    return render_template('option.html')
@app.route('/uploads', methods = ['GET', 'POST'])
def upload_file():
    import pdb
    pdb.set_trace()
    if request.method == 'GET':
        with open('C:/Users/ADMIN/Desktop/js.json','r') as f:
            data=f.read()
            print(data)
        #x=json.dump(data,f)
        return redirect(url_for('create'))

#@app.route('/uploads',methods=['POST','GET'])
#def upload_file():
    #if request.method=='GET':
     #   x1=input("enter the audiofilename: ")
      #  url='https://'+x1
       # data1=request.get(url)
        #data2=json.loads(data1.read())
        #print(data2)
        #return redirect(url_for('create')),data2

    #return render_template('upload.html')

#@app.route('/uploads',methods=['POST','GET'])
#def upload_file():
    #import pdb
    #pdb.set_trace()
    #if request.method=='GET':
        #r = requests.get('https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3')
        # x=json.loads(r.text)
        # return redirect(url_for('create'),x=x)

'''@app.route('/uploads',methods=['POST','GET'])
def upload_file():
    import pdb
    pdb.set_trace()
    if request.method=='GET':
         r = requests.get('https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3').json()
         #x=json.loads(r)
         print(r)
         return redirect(url_for('create'))'''
 

@app.route('/api/create',methods=['POST','GET'])
def create():
    #bal=0
    import pdb
    pdb.set_trace()
    if request.method=='GET':
        #data1=request.args.get('file')
        data1=request.json #taking data from server using json fomat
        #data=json.dumps(data1)
        #if data is 'Nonetype':
            #x=input()
            #r=requests.get(x).json
            #return redirect(url_for('create'))
        print(data1)
        data=json.dumps(data1)
        print(data)
        type=data.get(audioFileType,None)  # findinng the type of file
        if type is None:
            return 'the request is invalid:400 bad request',400
        aud_type=audiofiletype.get(type)  #checking the type of file is existing in audiofiletype 
        metadata = data.get("audioFileMetadata") 


        if metadata['duration_time']<0:
            metadata['duration_time']=0
        metadata['uploaded_time']=datetime.datetime.utcnow()

        if type=='song':
            name = metadata.get("Name_of_the_song", None)
            if (name is None or len(name) > 100):
                return "The request is invalid: 400 bad request",400
            try:
                aud_obj=Song(**metadata)
                db.session.add(aud_obj)
                db.session.commit()
                return '200 OK', 200
            except:
                return "The request is invalid: 400 bad request", 400
        return "The request is invalid: 400 bad request", 400



@app.route('/api/update/<audioFileType>/<audioFileID>',methods=['PUT'])
def update(audioFileType, audioFileID):
    
    if request.method=='PUT':
        request_data=request.get_json()
        if audioFileType not in audiofiletype:
            return "The request is invalid: 400 bad request", 400
        audio_file_obj = audiofiletype.get(audioFileType)

        try:
            audio_obj = audio_file_obj.query.filter_by(id=int(audioFileID))
            if not metadata:
                return "The request is invalid: 400 bad request", 400
            audio_obj.update(dict(metadata))
            db.session.commit()
            return "200 ok", 200
        except:
            return "The request is invalid: 400 bad request", 400
    return "The request is invalid: 400 bad request", 400





          

@app.route('/api/delete/<audioFileType>/<audioFileID>', methods=["DELETE"])
def delete_api(audioFileType, audioFileID):
        if request.method=='DELETE':
            if audioFileType not in audiofiletype:
                return "The request is invalid: 400 bad request", 400
            audio_file_obj = audiofiletype.get(audioFileType)
            try:
                audio_obj = audio_file_obj.query.filter_by(id=int(audioFileID)).one()
                if not audio_obj:
                    return "The request is invalid: 400 bad request", 400
                audio_obj.delete()
                db.session.commit()
                return "200 ok", 200
            except:
                return "The request is invalid: 400 bad request", 400
        return "The request is invalid: 400 bad request", 400

    
@app.route("/api/get/<audioFileType>", methods=["GET"], defaults={"audioFileID": None})
def get_api(audioFileType, audioFileID):
    if request.method=='GET':
        if audioFileType not in audiofiletype:
            return "The request is invalid: 400 bad request", 400
        audio_obj = audiofiletype.get(audioFileType)
        data = None
        try:
            if audioFileID is not None:
                data = audio_obj.query.filter_by(id=int(audioFileID)).one()
                data = [data.as_dict()]
            else:
                data = audio_obj.query.all()
                data = [dict(i) for i in data]
            return jsonify({"data": data}), 200
        except:
            return "The request is invalid: 400 bad request", 400
    return "The request is invalid: 400 bad request", 400



'''@app.route("/choices/<option>",metods=['POST','GET'])
def choices():
    if request.method=='POST':
        if option == 'create':
            data = request.json

            f=request.files['file']
            data1=f.save(secure_filename(f.filename))
            c2=song(name)
            db.session.add(c2)
            db.session.commit()
            return 'file uploaded successfull'
        elif option=='update':
            data1=song.query.get()
            data1.f=data1
            db.session.commit()
        elif option=='get_api':
            data1=song.query.get()
            return data1
        elif option=='delete':
            data1=song.query.get()
            db.session.delete()
            db.session.commit()'''










if __name__=='__main__':
    db.create_all()
    app.run(debug=True)


                
             
             
        
