#!/usr/bin/env bash
set -ex

## remove build directory
rm -rf build

## genrate js
rm -rf dist
yarn build

## build for 64bit
pkg --out-path build package.json --targets \
node16-linux-x64,\
node16-alpine-x64,\
node16-macos-x64

# windows backward compatible builds
npx pkg@4.5.1 --out-path build package.json --target node14-win-x64

## archive builds
cd build
for file in *; do
  du -sh $file
  if [[ $file == *".exe"* ]]; then
    if [[ $file != d-fi.exe ]]; then
      mv $file d-fi.exe
      zip ${file%.*}.zip d-fi.exe
    else
      zip d-fi-win.zip d-fi.exe
    fi
    rm d-fi.exe
  else
    mv $file d-fi
    zip ${file%.*}.zip d-fi
    rm d-fi
  fi
done
du -sh *
