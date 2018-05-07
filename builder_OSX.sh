py2applet --make-setup --argv-emulation=0 --iconfile=Gryn.icns Gryn.py
python setup.py py2app 

cd dist

ditto --rsrc --arch x86_64 Gryn.app Gryn_x86_64.app
rm -rf Gryn.app
mv Gryn_x86_64.app Gryn.app

# Fixed wrong path in Info.plist
cd Gryn.app/Contents
awk '{gsub("Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python", "@executable_path/../Frameworks/Python.framework/Versions/2.7/Python")}1' Info.plist > Info.plist_tmp && mv Info.plist_tmp Info.plist

cd ../../..

ln -s /Applications dist

mv dist Gryn_1.2

hdiutil create "Gryn_1.2.dmg" -srcfolder "Gryn_1.2"

rm -r build 
rm setup.py
rm -rf Gryn_1.2


