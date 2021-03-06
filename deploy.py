import argparse
import subprocess


def deploy(*, dry_run):
    cmd = [
        "rsync",
        "--itemize-changes",
        "--recursive",
        "--delete",
        "build/html/",
        "dedi3:/srv/nginx/html/python",
    ]
    if dry_run:
        cmd.append("--dry-run")
    print(*cmd)
    subprocess.run(cmd, check=True)

    cmd = [
        "scp",
        "build/latex/programmationenpython.pdf",
        "dedi3:/srv/nginx/html/python/cours-python.pdf",
    ]
    print(*cmd)
    if not dry_run:
        subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    deploy(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
