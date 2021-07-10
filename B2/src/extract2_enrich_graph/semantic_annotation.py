import requests

token = '76df1f8b-d548-4db5-8aba-af5e8f468e94-843339462' # colocar aquí el token
url_endpoint = 'https://tagme.d4science.org/tagme/tag?lang=en&include_abstract=true&include_categories=true&gcube-token='
headers = {'user-agent': 'Mozilla/5.0', 'accept': 'application/json', 'content-type': 'application/json'}
dbr = 'http://dbpedia.org/resource/'
dbc = 'http://dbpedia.org/resource/Category:'

def getAnnotationsAbstract (paper_id, text):
    url = url_endpoint + token + '&text=' + text

    resp = requests.get(url, headers=headers).json()
    resp.keys()
    annotations = resp['annotations']

    dbCategories = []

    for i in range(len(annotations)):
        ann = annotations[i]['spot']
        if annotations[i]['rho'] > 0.3 and annotations[i]['link_probability'] > 0.3:
            ann = ann.capitalize()
            ann = dbr + ann.replace(' ', '_')
            # Guardar como recursos de la Dbpedia:
            for c in annotations[i]['dbpedia_categories']:
                # dbCategories.append([paper_id, ann, annotations[i]['rho'],
                #                      annotations[i]['link_probability'], dbc + c.replace(' ', '_')])
                status = requests.get(ann)
                if status.status_code == 200:
                    dbCategories.append([ann, dbc + c.replace(' ', '_')])
                break
    return dbCategories

def getAnnotations(paper_id, text):
    url = url_endpoint + token + '&text=' + text

    resp = requests.get(url, headers=headers).json()
    resp.keys()
    annotations = resp['annotations']

    dbCategories = []

    for i in range(len(annotations)):
        ann = annotations[i]['spot']
        if annotations[i]['rho'] > 0.1 and annotations[i]['link_probability'] > 0.1:
            ann = ann.capitalize()
            ann = dbr + ann.replace(' ', '_')
            # Guardar como recursos de la Dbpedia:
            for c in annotations[i]['dbpedia_categories']:
                # dbCategories.append([paper_id, ann, annotations[i]['rho'],
                #                      annotations[i]['link_probability'], dbc + c.replace(' ', '_')])
                status = requests.get(ann)
                if status.status_code == 200:
                    dbCategories.append([ann, dbc + c.replace(' ', '_')])
                break
    return dbCategories