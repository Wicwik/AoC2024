from PIL import Image

import glob


def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")][:8149]
    frame_one = frames[0]
    frame_one.save("robots.gif", format="GIF", append_images=frames,
               save_all=True, duration=.5, loop=0)
    
if __name__ == "__main__":
    make_gif("./imgs")