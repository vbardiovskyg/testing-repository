import sys

def main(argv):
  print("Running...")
  print(argv)

  for filename in argv[1:]:
    if "submit" not in filename:
      raise ValueError("Must contain 'submit' in name.")

if __name__ == '__main__':
  main(sys.argv)
