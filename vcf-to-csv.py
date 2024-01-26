import csv
import sys
import vobject

def vcf_to_csv(vcf_filename, csv_filename):
    with open(vcf_filename, 'r') as vcf_file:
        vcf_text = vcf_file.read()
        vcf_contacts = vobject.readComponents(vcf_text)

        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['first_name', 'phone_numbers', 'email', 'url', 'ab_label', 'social_profiles'])
            for vcf_contact in vcf_contacts:
                first_name = vcf_contact.fn.value if hasattr(vcf_contact, 'fn') else ''
                phone_numbers = vcf_contact.tel.value if hasattr(vcf_contact, 'tel') else ''
                email = vcf_contact.email.value if hasattr(vcf_contact, 'email') else ''
                url = vcf_contact.url.value if hasattr(vcf_contact, 'url') else ''
                ab_label = getattr(vcf_contact, 'x-ablabel').value if hasattr(vcf_contact, 'x-ablabel') else ''
                social_profiles = getattr(vcf_contact, 'x-socialprofile').value if hasattr(vcf_contact, 'x-socialprofile') else ''
                writer.writerow([first_name, phone_numbers, email, url, ab_label, social_profiles])


if __name__ == "__main__":
    vcf_file = sys.argv[1]
    csv_file = sys.argv[2]
    vcf_to_csv(vcf_file,csv_file)