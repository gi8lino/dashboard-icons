from pathlib import Path


def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" width="50">'


if __name__ == "__main__":
    imgs = sorted(Path("../png").glob("*.png"))
    img_tags = [generate_img_tag(x) for x in imgs]

    with open("README.md", "wt", encoding="UTF-8") as f:
        f.write("# Dashboard Icons\n\n")
        f.write("### The best Dashboards:\n\n")
        f.write("[- Homer Dashboard](https://github.com/bastienwirtz/homer)\n")
        f.write("[- Heimdall](https://github.com/linuxserver/Heimdall)\n")
        f.write("[- Organizr (v2)](https://github.com/causefx/Organizr)\n")
        f.write("[- Dashy](https://github.com/Lissy93/dashy)\n")
        f.write("[- Flame](https://github.com/pawelmalak/flame)\n")
        f.write("[- Tinyhome](https://github.com/bderenzo/tinyhome)\n")
        f.write("[- SUI](https://github.com/jeroenpardon/sui)\n\n")
        f.write(" ".join(img_tags))
        f.write("\n")
