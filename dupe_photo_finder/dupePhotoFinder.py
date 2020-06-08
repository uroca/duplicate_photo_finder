import sys
import controller as c
import view as v


if __name__ == "__main__":
    controller = c.Controller()
    view_parent = v.Parent(controller)
