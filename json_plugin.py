import uuid
import json
uuid = uuid.uuid4()
print(uuid)


def manifest(id_:str,version:float,title:str,platforms,text:str,autor:str,thumbnail:str):
    def platforms_type(platforms_date):
        if isinstance(platforms,str):
            return [platforms]
        if isinstance(platforms,list):
            return platforms
        else:
            raise TypeError('Platform must be a string or a list')
    info = {
        'id': id_,
        'version': version,
        'title': title,
        'platforms': platforms_type(platforms),
        'text': text,
        'autor': autor,
        'thumbnail': thumbnail
    }
    return json.dumps(info,indent=4)

with open("manifest.manifest","w") as f:
    f.write(manifest("hola",0.1,"asdasda",["afsdfas","ssdasd"],"asd","ads","dsfs"))