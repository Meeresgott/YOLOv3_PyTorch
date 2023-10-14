import sys
import requests
import argparse


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download&confirm=1"

    session = requests.Session()

    response = session.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def main():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
        
    parser.add_argument('-n', '--net', help='You can choose from three nets to download: \n 1. YOLO v3 weights base on darknet_53 backbone \n 2. darknet53_weights_pytorch.pth \n 3.official_yolov3_weights_pytorch.pth')
    
    args = parser.parse_args()
    if args.net is None:
        print(f'you have to choose a net to download')
        return
    elif int(args.net) == 1:
        file_id = "1Bm_CLv9hP3mMQ5cyerKRjvt7_t1duvjI"
        destination = "yolov3_weights_pytorch.pth"
    elif int(args.net) == 2:
        file_id = "1VYwHUznM3jLD7ftmOSCHnpkVpBJcFIOA"
        destination = "darknet53_weights_pytorch.pth"
    elif int(args.net) == 3:
        file_id = "1SnFAlSvsx37J7MDNs3WWLgeKY0iknikP"
        destination = "official_yolov3_weights_pytorch.pth"
    else:
        print(f'Choose 1. 2. or 3. - Your are out of range')
        return
        
        
    print(f"dowload {file_id} to {destination}")
    download_file_from_google_drive(file_id, destination)


if __name__ == "__main__":
    main()
