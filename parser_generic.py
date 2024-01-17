# -*- coding: utf-8 -*-
"""parser_generic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SKJ1l9iWiUtA7QpChVHn0j7tdnu99hZF
"""

import abc
import re
#Parent class for all medical document
class MedicalDocParser(metaclass=abc.ABCMeta):
  def __init__(self,text):
    self.text = text
  @abc.abstractmethod

  def parse(self):
    pass

#Child class for Presciption documents
class PrescriptionParser(MedicalDocParser):
  def __init__(self,text):
    MedicalDocParser.__init__(self,text)
  def parse(self):
    return {
        'patient_name': self.get_field('patient_name'),
        'address': self.get_field('address'),
        'medicine': self.get_field('medicine'),
        'directions': self.get_field('directions'),
        'refill': self.get_field('refills')
    }
  def get_field(self, field_name):
    pattern = ''
    flags = 0
    pattern_dict = {
        'patient_name':{'pattern':"Name:(.*)Date",'flags': 0},
        'address':{'pattern':"Address:(.*)\n",'flags':0},
        'medicine': {'pattern':"Address:[^\n]*(.*)Directions",'flags':re.DOTALL},
        'directions':{'pattern':"Directions:(.*)Refill",'flags':re.DOTALL},
        'refills':{'pattern':"Refill:(.*)times",'flags':0}
    }
    pattern_object = pattern_dict.get(field_name)
    if pattern_object:
      matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
      if len(matches)>0:
        return matches[0].strip()

#Child class for Patient detail documents
class PatientDetailsParser(MedicalDocParser):
  def __init__(self,text):
    MedicalDocParser.__init__(self,text)
  def parse(self):
    return {
        'patient_name': self.get_patient_name(),
        'birthday': self.get_birthday(),
        'phone': self.get_phone(),
        'hepatitis_b_vaccination': self.get_hep_b_vaccination(),
        'medical_probs': self.get_medical_probs()
    }

  def remove_noise_extract_name_birthday(self,name):
    name = name.strip()
    filter = "[^0-9](.*)"
    name = re.findall(filter, name, flags=re.DOTALL)
    name = name[0].strip() #remove any leading or trailing whitespace
    #Birthday extraction
    birthday_pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [ \d]+)'
    birthday_matches = re.findall(birthday_pattern, name)
    if birthday_matches:
      birthday = birthday_matches[0][0]
      #Patient name extraction
      patient_name = name.replace(birthday, "").strip()
      return patient_name, birthday

  def get_patient_name(self):
    pattern_name = "Birth Date(.*?)\(\d{3}\)"
    name = re.findall(pattern_name, self.text, flags=re.DOTALL)
    name = name[0]
    if name:
      patient_name, birthday = self.remove_noise_extract_name_birthday(name)
      return patient_name

  def get_birthday(self):
    pattern_name = "Birth Date(.*?)\(\d{3}\)"
    name = re.findall(pattern_name, self.text, flags=re.DOTALL)
    name = name[0]
    if name:
      patient_name, birthday = self.remove_noise_extract_name_birthday(name)
      return birthday

  def get_phone(self):
    pattern_phone = "Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})"
    match = re.findall(pattern_phone, self.text, flags=re.DOTALL)
    if match:
      return match[0][1]

  def get_hep_b_vaccination(self):
    pattern_vaccine = "Have you had the Hepatitis B vaccination\?.*(No|Yes)"
    match = re.findall(pattern_vaccine, self.text,  flags=re.DOTALL)
    if match:
      return match[0].strip() #remove any leading or trailing whitespace

  def get_medical_probs(self):
    pattern_medical_probs = "List any Medical Problems \(asthma, seizures, headaches[\}|[\)]:(.*)"
    match = re.findall(pattern_medical_probs, self.text, flags=re.DOTALL)
    if match:
      return match[0].strip() #remove any leading or trailing whitespace