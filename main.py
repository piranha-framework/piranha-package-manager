#!/usr/bin/python

from src import git
import optparse

def main():
    flag = optparse.OptionParser()
    flag.add_option('--person', '-p',default="world")
    flag.add_option('--makemigrations','-M') # This will generate the migration informations 
    flag.add_option('--migrate', '-m') # This will do the actual migration in database

    options,arguments = flag.parse_args()
    print("Hello %s"% options.person)
    print("Hello %s"%arguments)
#    git.clone_repo()

if __name__ == "__main__":
    main()
