from PIL import Image

def scale_gif(path, scale, new_path=None):
    gif = Image.open(path)
    if not new_path:
        new_path = path
    if path[-3:] == "gif":
        old_gif_information = {
            'loop': bool(gif.info.get('loop', 1)),
            'duration': gif.info.get('duration', 40),
            'background': gif.info.get('background', 223),
            'extension': gif.info.get('extension', (b'NETSCAPE2.0')),
            'transparency': gif.info.get('transparency', 223)
        }
        new_frames = get_new_frames(gif, scale)
        save_new_gif(new_frames, old_gif_information, new_path)
    else:
        transWidth = transform_width(gif.width, gif.height)  
        finalWidth = round(transWidth)
        gif = gif.resize((720, finalWidth))
        gif.save(path)
        
def transform_width(width, height):
    multiple = find_proportion(720, height)
    return width * multiple


def find_proportion(baseH, h):
    return baseH/h
     


def get_new_frames(gif, scale):
    new_frames = []
    actual_frames = gif.n_frames
    for frame in range(actual_frames):
        gif.seek(frame)
        new_frame = Image.new('RGBA', gif.size)
        new_frame.paste(gif)
        transWidth = transform_width(new_frame.width, new_frame.height)  
        finalWidth = round(transWidth)
        new_frame = new_frame.resize(scale, Image.ANTIALIAS)
        new_frames.append(new_frame)
    return new_frames

def save_new_gif(new_frames, old_gif_information, new_path):
    new_frames[0].save(new_path,
                       save_all = True,
                       append_images = new_frames[1:],
                       duration = old_gif_information['duration'],
                       loop = old_gif_information['loop'],
                       background = old_gif_information['background'],
                       extension = old_gif_information['extension'] ,
                       transparency = old_gif_information['transparency'])


if __name__ == "__main__":
    scale_gif(f"Post-qtehpj.gif", (1280,720),"test.gif")