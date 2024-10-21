{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "49621fae-e74b-44b6-8e97-28949c149a76",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 33\n",
    "b = 100\n",
    "if (a>b):\n",
    "    print(\"Nilai A lebih Besar dari B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7656c509-71ad-4d69-a869-45e6127ade43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nilai A lebih Kecil dari B\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 100\n",
    "if (a>b):\n",
    "    print(\"Nilai A lebih Besar dari B\")\n",
    "else:\n",
    "    print(\"Nilai A lebih Kecil dari B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "87967e23-eaee-4574-a136-c3a4dbb80923",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nilai A lebih Besar dari B\n"
     ]
    }
   ],
   "source": [
    "a = 100\n",
    "b = 50\n",
    "if (a>b):\n",
    "    print(\"Nilai A lebih Besar dari B\")\n",
    "else:\n",
    "    print(\"Nilai A lebih Kecil dari B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "00a5209c-3c3c-434a-a26c-f15b550a648e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nilai A lebih Besar dari B\n"
     ]
    }
   ],
   "source": [
    "a = 100\n",
    "b = 50\n",
    "if (a>b):\n",
    "    print(\"Nilai A lebih Besar dari B\")\n",
    "elif (a<b):\n",
    "    print(\"Nilai A lebih Kecil dari B\")\n",
    "else:\n",
    "    print(\"Nilai A Sama Dengan B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2d36d2b1-4b97-42e0-bb1a-18e750e92092",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A lebih Besar dari B\n"
     ]
    }
   ],
   "source": [
    "if (a>b) : print(\"A lebih Besar dari B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c27ab334-02fc-4764-bbab-99ec978ef659",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A lebih Besar dari B\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 5\n",
    "\n",
    "print(\"A lebih Besar dari B\") if a>b else print(\"A lebih Kecil dari B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f0ac5563-4f6a-4632-aa5c-9e76e0ffbb07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A lebih Besar dari B\n"
     ]
    }
   ],
   "source": [
    "print(\"A lebih Besar dari B\") if a>b else print(\"A lebih Kecil dari B\") if a<b else print(\"A sama dengan B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4a1efc27-235f-4ee8-a759-ada8cbea4c46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bilangan Ganjil\n"
     ]
    }
   ],
   "source": [
    "bilangan = 25\n",
    "\n",
    "if (bilangan %2 ==0):\n",
    "    print(\"Bilangan Genap\")\n",
    "else:\n",
    "    print(\"Bilangan Ganjil\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7618909f-9178-4b47-a606-299ea69f0e09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Masukkan Nama Anda :  Dimas Kurnia Putra\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nama Anda Adalah : Dimas Kurnia Putra\n"
     ]
    }
   ],
   "source": [
    "nama = input (\"Masukkan Nama Anda : \")\n",
    "print (\"Nama Anda Adalah : \" + nama)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7cc8725e-830b-42b4-92a7-09ad82b3012a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Masukkan Bilangan :  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 Adalah Bilangan Genap\n"
     ]
    }
   ],
   "source": [
    "bilangan = int (input(\"Masukkan Bilangan : \"))\n",
    "\n",
    "if (bilangan %2 == 0):\n",
    "    print(bilangan, \"Adalah Bilangan Genap\")\n",
    "else:\n",
    "    print(bilangan, \"Adalah Bilangan Ganjil\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
