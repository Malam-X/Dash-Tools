"""
  DASH TOOLS
  Author: Author: DR4G0N5, JARED, Bomb SQU4D
  Version: 0.0.4
"""
import sys
import var
import about
def main():
    try:
        while True:
            var.print_lines()
            print(
                "\t",
                var.PyColors.bold,
                var.PyColors.Fg.light_yellow,
                " <<< Network TNA >>>",
                var.PyColors.reset,
                "\n\t",
                var.PyColors.Fg.light_green,
                "  Project Version | Last Updated\n\t",
                "  Version: 0.0.4",
                var.PyColors.reset
            )
            first_choice = input(
                "\n 1) About"
                "\n 2) Quit"
                "\n\n [+] Choice: "
            ).strip()
            if first_choice == "1":
                about.main()
            elif first_choice == "2":
                print("\n\n [!] Exiting program\n")
                sys.exit(0)
    except KeyboardInterrupt:
        print("\n\n [!] Exiting program\n")
        sys.exit(0)
if __name__ == "__main__":
    main()
