import java.util.*;
import java.io.*;

class ip_add {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int ip[] = new int[4];
        int mask1[] = new int[4];
        int first_add[] = new int[4];
        int last_add[] = new int[4];
        int comp_mask[] = new int[4];
        String binary_mask = "";
        String mask_comp = "";
        int i = 0, j = 0, k = 0;
        System.out.println("1. Binary Notation");
        System.out.println("2. Decmimal-dotted Notation");
        System.out.print("Choose the format in which you want to enter IPv4 Address: ");
        String choise = sc.nextLine();
        int choose = Integer.parseInt(choise);
        System.out.print("Enter the IPv4 Address: ");
        String ip_str = sc.nextLine();
        System.out.print("Enter the mask to find first, last address: ");
        String mask = sc.nextLine();
        int maskint = Integer.parseInt(mask);
        for (int x = 0; x < 32; x++) {
            if (x < maskint) {
                binary_mask = binary_mask + '1';
            } else {
                binary_mask = binary_mask + '0';
            }
        }
        mask1[0] = Integer.parseInt(binary_mask.substring(0, 8), 2);
        mask1[1] = Integer.parseInt(binary_mask.substring(8, 16), 2);
        mask1[2] = Integer.parseInt(binary_mask.substring(16, 24), 2);
        mask1[3] = Integer.parseInt(binary_mask.substring(24, 32), 2);
        for (int x = 0; x < 32; x++) {
            if (x < maskint) {
                mask_comp = mask_comp + '0';
            } else {
                mask_comp = mask_comp + '1';
            }
        }
        comp_mask[0] = Integer.parseInt(mask_comp.substring(0, 8), 2);
        comp_mask[1] = Integer.parseInt(mask_comp.substring(8, 16), 2);
        comp_mask[2] = Integer.parseInt(mask_comp.substring(16, 24), 2);
        comp_mask[3] = Integer.parseInt(mask_comp.substring(24, 32), 2);
        switch (choose) {
            case 1:
                while (j != 3) {
                    while (i < ip_str.length() && ip_str.charAt(i++) == '.') {
                        ip[j++] = Integer.parseInt(ip_str.substring(k, i - 1), 2);
                        k = i;
                    }
                }
                ip[j++] = Integer.parseInt(ip_str.substring(k, ip_str.length()), 2);
                for (int x = 0; x < 4; x++) {
                    first_add[x] = ip[x] & mask1[x];
                }
                System.out.println();
                System.out.println("Output");
                System.out.println("The First Address is: " + first_add[0] + "." + first_add[1] + "." + first_add[2]
                        + "." + first_add[3]);
                for (int x = 0; x < 4; x++) {
                    last_add[x] = ip[x] | comp_mask[x];
                }
                System.out.println("The Last Address is: " + last_add[0] + "." + last_add[1] + "." + last_add[2] + "."
                        + last_add[3]);
                break;
            case 2:
                while (j != 3) {
                    while (i < ip_str.length() && ip_str.charAt(i++) == '.') {
                        ip[j++] = Integer.parseInt(ip_str.substring(k, i - 1));
                        k = i;
                    }
                }
                ip[j++] = Integer.parseInt(ip_str.substring(k, ip_str.length()));
                for (int x = 0; x < 4; x++) {
                    first_add[x] = ip[x] & mask1[x];
                }
                System.out.println();
                System.out.println("Output");
                System.out.println("The First Address is: " + first_add[0] + "." + first_add[1] + "." + first_add[2]
                        + "." + first_add[3]);
                for (int x = 0; x < 4; x++) {
                    last_add[x] = ip[x] | comp_mask[x];
                }
                System.out.println("The Last Address is: " + last_add[0] + "." + last_add[1] + "." + last_add[2] + "."
                        + last_add[3]);
                break;
            default:
                System.out.println("Invalid IP Address");
        }
    }
}

