CC=gcc
CCFLAGS=-c

DBRLIB_PATH=../../../lib/WITHSTDC++LIB
LDFLAGS=-L $(DBRLIB_PATH) -Wl,-rpath=$(DBRLIB_PATH) -Wl,-rpath=./
DBRLIB=-lDynamsoftBarcodeReader

STDLIB=-lstdc++

TARGET=ReadMultiBarcodes
OBJECT=ReadMultiBarcodes.o
SOURCE=ReadMultiBarcodes.cpp

# build rule for target.
$(TARGET): $(OBJECT)
	$(CC) -o $(TARGET) $(OBJECT) $(STDLIB) $(DBRLIB) $(LDFLAGS)

# target to build an object file
$(OBJECT): $(SOURCE)
	$(CC) $(CCFLAGS) $(SOURCE)

# the clean target
.PHONY : clean
clean: 
	rm -f $(OBJECT) $(TARGET)

