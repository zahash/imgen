import argparse
from .imgen import generate

ap = argparse.ArgumentParser(allow_abbrev=False)
ap.add_argument(
    "-f",
    "--filepath",
    type=str,
    required=True,
    help="generated image will be saved to this filepath",
)
ap.add_argument(
    "-rh",
    "--resh",
    type=int,
    required=True,
    help="horizontal resolution",
)
ap.add_argument(
    "-rv",
    "--resv",
    type=int,
    required=True,
    help="vertical resolution",
)
ap.add_argument("-d", "--darkmode", action="store_true")
ap.add_argument("-s", "--seed", type=str, default=None, help="seed for random")
args = ap.parse_args()

img = generate(args.resh, args.resv, args.darkmode, args.seed)
optimize = args.filepath.lower().endswith(".png")  # png has lossless compression
img.save(args.filepath, optimize=optimize)
