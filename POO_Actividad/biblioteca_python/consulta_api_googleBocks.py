import requests

def buscar_libros(query, max_resultados=10):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': query,
        'maxResults': max_resultados
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        libros = []
        for item in data.get('items', []):
            libro_info = {
                'titulo': item['volumeInfo']['title'],
                'autores': item['volumeInfo'].get('authors', ['Autor desconocido']),
                'fecha_publicacion': item['volumeInfo'].get('publishedDate', 'Fecha desconocida')
            }
            libros.append(libro_info)
        return libros
    else:
        print('Error al realizar la solicitud:', response.status_code)

# Ejemplo de búsqueda de libros con el término "Python"
libros_encontrados = buscar_libros('Python', max_resultados=5)
for libro in libros_encontrados:
    print( libro['titulo'])
    print(', '.join(libro['autores']))
    print( libro['fecha_publicacion'])
    print('---')
