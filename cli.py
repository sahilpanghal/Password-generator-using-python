import typer
from passwordGenerator import passwordGenerator


def passwordGeneratorCLI():
    passwordLenght = typer.prompt("\nPassword lenght 📶")
    upperCasesConfirm = typer.confirm("Uppercases 🔠")
    lowerCasesConfirm = typer.confirm("Lowercases 🔡")
    numbersConfirm = typer.confirm("Numbers 🔢")
    specialCharactersConfirm = typer.confirm("Symbols 🔣")
    print(
        "\nPassword 🔑: "
        + "\033[92m"
        + passwordGenerator(
            int(passwordLenght),
            lowerCasesConfirm,
            upperCasesConfirm,
            numbersConfirm,
            specialCharactersConfirm,
        )
        + "\033"
    )


if __name__ == "__main__":
    typer.run(passwordGeneratorCLI)
