#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
    int size, allocaton, index;
    Python *pythonObject;

    size = Py_SIZE(p);
    allocaton = PyList_Alloc(p);
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocaton);

    index = 0;

    while (index < size)
    {
        pythonObject = PyList_GetItem(p, index);
        printf("Element %d: %s\n", index, PyTYPE(pythonOject));
        index++;
    };
}