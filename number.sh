#!/bin/bash 

# Generate array with static values from 1 to 10
num_array=()
for i in {1..10}
do
	num_array+=($i)
done

# Shufle the array
num_array=( $(shuf -e "${num_array[@]}") )
echo "${num_array[@]}"


