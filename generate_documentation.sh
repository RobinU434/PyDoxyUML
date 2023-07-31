# all given arguments have to be source directories
DIRS=$@
echo defined src directories are: ${DIRS[@]} 

DOCU_DIR="./documentation"

echo generate uml diagrams
UML_DIR="${DOCU_DIR}/uml"
mkdir -p $UML_DIR
python -m documentation.generate_uml $DIRS

TMP_SRC=$DOCU_DIR/tmp
echo $TMP_SRC
# find all source files
FILES=$(find ${DIRS[@]} -name "*.py")

echo create tmp source directories
for FILE in ${FILES[@]}
do
    mkdir -p $TMP_SRC/${FILE%/*}
done

echo convert docstring into doxygen format
for FILE in $FILES
do
    echo $FILE
    $(doxypypy -a -c $FILE > "$TMP_SRC/$FILE")
done

echo generate documentation
cd $DOCU_DIR
doxygen Doxyfile
cd ..

echo build Latex pdf
cd $DOCU_DIR/latex
make
cd ../..

echo remove tmp directory
rm -rf $TMP_SRC