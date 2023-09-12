#include <Python.h>

/**
 * print_python_list_info - ....
 * @p:...
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	long int len, i;
	PyObject *item;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
