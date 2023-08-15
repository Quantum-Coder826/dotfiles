#!/bin/bash

for i in {0..7..1}
do
	ratbagctl warbling-mara button "$i" get
done
