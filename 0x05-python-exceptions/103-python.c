#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - This function gives data of the python list object
 * @p: the PyObject
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}



/**
 * print_python_bytes - This function gives data of the python bytes object
 * @p: the PyObject
 *
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %d bytes: ", size > 10 ? 10 : (int)size);
	for (i = 0; i < (size > 10 ? 10 : size); i++) {
		printf("%02x%c", str[i] & 0xff, i == (size > 10 ? 9 : size - 1) ? '\n' : ' ');
	}
}



/**
 * print_python_float - This function gives data of the python float object
 * @p: the PyObject
 *
 * Return: Nothing
 */

void print_python_float(Pyobject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %lf\n", ((PyFloatObject *)p)->ob_fval);
}
