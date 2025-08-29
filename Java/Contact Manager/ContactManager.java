import java.io.*;
import java.util.*;

public class ContactManager {
    private static final String FILE_PATH = "contacts.txt";

    public ContactManager() {
        File file = new File(FILE_PATH);
        try {
            if (!file.exists()) {
                file.createNewFile();
            }
        } catch (IOException e) {
            System.out.println("Error initializing contact file.");
        }
    }

    public void addContact(String name, String phone) {
        if (searchContactByPhone(phone) != null) {
            System.out.println("A contact with this phone number already exists.");
            return;
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_PATH, true))) {
            writer.write(name + "," + phone);
            writer.newLine();
            System.out.println("Contact added: " + name + " - " + phone);
        } catch (IOException e) {
            System.out.println("Error adding contact.");
        }
    }

   public void favouritecontacts(String name,String phone){
        if (searchContactByPhone(phone) != null) {
            System.out.println("A contact with this phone number exists.");
            
            return;
        }
    }

    public void editContact(String identifier, String newName, String newPhone) {
        File inputFile = new File(FILE_PATH);
        File tempFile = new File("temp.txt");
    
        boolean contactFound = false;
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             BufferedWriter writer = new BufferedWriter(new FileWriter(tempFile))) {
    
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                String[] contact = currentLine.split(",");
                String name = contact[0];
                String phone = contact[1];
    
                // Check if identifier matches either name or phone
                if (phone.equals(identifier) || name.equalsIgnoreCase(identifier)) {
                    contactFound = true;
                    String updatedName = (newName != null && !newName.isEmpty()) ? newName : name;
                    String updatedPhone = (newPhone != null && !newPhone.isEmpty()) ? newPhone : phone;
    
                    // Write the updated contact to the temp file
                    writer.write(updatedName + "," + updatedPhone);
                    System.out.println("Contact updated: " + updatedName + " - " + updatedPhone);
                } else {
                    // Write the unchanged contact to the temp file
                    writer.write(currentLine);
                }
                writer.newLine();
            }
    
            if (!contactFound) {
                System.out.println("Contact not found.");
            }
    
        } catch (IOException e) {
            System.out.println("Error editing contact.");
        }
    
        // Replace the old file with the updated temp file if changes were made
        if (contactFound) {
            if (inputFile.delete() && tempFile.renameTo(inputFile)) {
                System.out.println("Contact file updated successfully.");
            } else {
                System.out.println("Error updating the contact file.");
            }
        } else {
            tempFile.delete();
        }
    }
    

    public void deleteContact(String identifier) {
        File inputFile = new File(FILE_PATH);
        File tempFile = new File("temp.txt");
    
        boolean contactFound = false;
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             BufferedWriter writer = new BufferedWriter(new FileWriter(tempFile))) {
    
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                String[] contact = currentLine.split(",");
                String name = contact[0];
                String phone = contact[1];
    
                // Check if the identifier matches either the name or phone
                if (phone.equals(identifier) || name.equalsIgnoreCase(identifier)) {
                    contactFound = true;
                    System.out.println("Deleted contact: " + name + " - " + phone);
                    continue; // Skip writing this line to delete the contact
                }
                writer.write(currentLine);
                writer.newLine();
            }
    
            if (!contactFound) {
                System.out.println("Contact not found.");
            }
    
        } catch (IOException e) {
            System.out.println("Error deleting contact.");
        }
    
        // Ensure the input file is properly replaced by the temp file
        if (contactFound) {
            if (inputFile.delete() && tempFile.renameTo(inputFile)) {
                System.out.println("Contact deleted successfully.");
            } else {
                System.out.println("Error updating the contact file.");
            }
        } else {
            // Clean up temp file if contact was not found
            tempFile.delete();
        }
    }
    

    public void searchContact(String query) {
        boolean found = false;

        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String currentLine;
            System.out.println("\nSearch Results:");

            while ((currentLine = reader.readLine()) != null) {
                String[] contact = currentLine.split(",");
                String name = contact[0];
                String phone = contact[1];

                if (name.toLowerCase().contains(query.toLowerCase()) || phone.contains(query)) {
                    System.out.println("   " + name + " - " + phone);
                    found = true;
                }
            }

            if (!found) {
                System.out.println("No matching contacts found.");
            }

        } catch (IOException e) {
            System.out.println("Error searching contacts.");
        }
    }

    public void displayContacts() {
        List<String> contacts = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                contacts.add(currentLine);
            }

            if (contacts.isEmpty()) {
                System.out.println("No contacts available.");
                return;
            }

            // Sort contacts alphabetically by name
            contacts.sort((c1, c2) -> {
                String name1 = c1.split(",")[0];
                String name2 = c2.split(",")[0];
                return name1.compareToIgnoreCase(name2);
            });

            System.out.println("\nAll Contacts along with their Phone Number:");
            for (String contact : contacts) {
                String[] contactInfo = contact.split(",");
                System.out.println("   " + contactInfo[0] + " - " + contactInfo[1]);
            }

        } catch (IOException e) {
            System.out.println("Error displaying contacts.");
        }
    }

    private String searchContactByPhone(String phone) {
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                String[] contact = currentLine.split(",");
                if (contact[1].equals(phone)) {
                    return currentLine;
                }
            }
        } catch (IOException e) {
            System.out.println("Error searching contact by phone.");
        }
        return null;
    }

    public static void main(String[] args) {
        ContactManager manager = new ContactManager();
        Scanner scanner = new Scanner(System.in);
        String choice;

        do {
            System.out.println("\n==================================");
            System.out.println("         CONTACT MANAGER          ");
            System.out.println("==================================");
            System.out.println("     1. Add Contact               ");
            System.out.println("     2. Edit Contact              ");
            System.out.println("     3. Delete Contact            ");
            System.out.println("     4. Search Contact            ");
            System.out.println("     5. Display Contacts          ");
            System.out.println("     6. Exit                      ");
            System.out.println("==================================");
            System.out.print("Choose an option: ");
            choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Enter name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter phone number: ");
                    String phone = scanner.nextLine();
                    manager.addContact(name, phone);
                    break;
                case "2":
                    System.out.print("Enter the phone number or name of the contact to be changed: ");
                    String oldPhone = scanner.nextLine();
                    System.out.print("Enter new name (leave blank to keep unchanged): ");
                    String newName = scanner.nextLine();
                    System.out.print("Enter new phone number (leave blank to keep unchanged): ");
                    String newPhone = scanner.nextLine();
                    manager.editContact(oldPhone, newName, newPhone);
                    break;
                case "3":
                    System.out.print("Enter the name or phone number of the contact to delete: ");
                    String identifier = scanner.nextLine();
                    manager.deleteContact(identifier);
                    break;
                
                case "4":
                    System.out.print("Enter name or phone number to search: ");
                    String query = scanner.nextLine();
                    manager.searchContact(query);
                    break;
                case "5":
                    manager.displayContacts();
                    break;
                case "6":
                    System.out.println("Exiting the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        } while (!choice.equals("6"));

        scanner.close();
    }
}
