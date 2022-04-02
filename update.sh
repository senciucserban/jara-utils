#!/bin/bash

function update_packages() {
  # Accepts 2 arguments, 1st - flags: string, 2nd - an array
  echo "Updating packages using flags $1"

  for i in "${@:2}"
  do
    echo "... ${i}"
    printf "\n\n>>>>>>>>>>>>>>> %s <<<<<<<<<<<<<<<\n" "$i" >> update_output.txt
    eval "poetry add ${i}@latest $1 >> update_output.txt"
    printf ">>>>>>>>>>>>>>> %s <<<<<<<<<<<<<<<\n\n" "$i" >> update_output.txt
  done
}

echo 'Start' > 'update_output.txt'

declare  -a required=(
  # Base packages
  "pytz" "types-pytz"
)
declare  -a optional=(
  "pytest" "pytest-cov" "pytest-asyncio" "faker" "bandit" "mypy"
  "flake8" "flake8-quotes" "flake8-pytest-style" "flake8-comprehensions" "flake8-multiline-containers" "flake8-builtins"
  "flake8-print" "flake8-debugger" "flake8-simplify" "flake8-annotations" "flake8-commas" "flake8-eradicate"
)
declare -a dev=("pytest-sugar" "pytest-deadfixtures" "ipython" "ipdb")


update_packages "" "${required[@]}"
update_packages "--optional" "${optional[@]}"
update_packages "-D" "${dev[@]}"

echo "Check the output in \`update_output.txt\` file"
echo 'End' >> 'update_output.txt'
