import requests

def get_coordinates(location:str):
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch?q=" + location
    coordinates = requests.get(url).json()

    return(coordinates)

def main():
    coo_list = get_coordinates("江戸川区")
    print(coo_list)
if __name__ == '__main__':
    main()
