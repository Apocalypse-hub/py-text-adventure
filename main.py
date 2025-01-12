import time


def main():
    boot_sequence()
    while True:
        try:
            handle(input("> "))()
        except KeyboardInterrupt:
            input("Press enter to shutdown...\n")
            exit()

def boot_sequence() -> None:
    print("Booting", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    print("Welcome to the Everyday General-purpose Operating System (or egOS for short)!\n(not to be confused with everyday genuine pieces of sh*t)\n\nEnter command below, type 'help' for available commands, or press ctrl+c to exit.\n")

def handle(str) -> callable:
    if str not in COMMAND_FUNC_MAP:
        return do_nothing
    return COMMAND_FUNC_MAP[str]


def do_nothing():
    print("invalid command, you might ask for 'help' :)")

def helper():
    print(f"The following commands are available:\n")
    for command in COMMAND_FUNC_MAP:
        print(command)


COMMAND_FUNC_MAP: dict[str, callable] = {
    "help" : helper
}
INVENTORY = []

if __name__ == "__main__":
    main()