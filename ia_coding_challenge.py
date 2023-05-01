orders = ['Rx1:MedicationX', 'Rx2:MedicationY', 'Rx3:MedicationZ', 'Rx4:MedicationA']
medications = ['MedicationA:1,2,3', 'MedicationX:1,2,', 'MedicationY:0', 'MedicationZ:3']

def create_labels(orders, medications):
  #Initialize list of order labels
  order_labels = []

  for order in orders:
    #Split orders into ID and name using ':' from string.
    order_id, order_name = order.split(':')
    #Initialize list of instructions
    instructions = []
    for medication in medications:
      #Split orders into name and handling instructions using ':' from string.
      medication_name, handling_instructions = medication.split(':')
      #If names for order and medication match, proceed with handling instructions
      if order_name == medication_name:
        #Iterate over handling instructions using ',' to separate individual instructions.
        for handling_instruction in handling_instructions.split(','):
          #Map handling instruction codes to respective instruction
          if handling_instruction == '1':
            instructions.append('Do Not Shake')
          elif handling_instruction == '2':
            instructions.append('Must Refrigerate')
          elif handling_instruction == '3':
            instructions.append('Keep Away From Heat')
    if len(instructions) > 0:
      if len(instructions) == 3:
        order_labels.append(f'{order_id}:{order_name}:WARNING!!!-{", ".join(instructions)}')
      else:
        order_labels.append(f'{order_id}:{order_name}:WARNING-{", ".join(instructions)}')
    else:
      order_labels.append(f'{order_id}:{order_name}:')
  return order_labels

print(create_labels(orders, medications))