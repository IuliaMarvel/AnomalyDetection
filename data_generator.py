import json
import random
import argparse


def generate_data(num_records):
    # Possible values for each field
    # TLSVersion,Ciphers,Extensions,EllipticCurves
    user_agents = [
        "Chrome (Android)",
        "Safari (iOS)",
        "Mozilla/5.0 (Windows)",
        "Mozilla/5.0 (MacOS)",
        "Mozilla/5.0 (Linux)"
    ]

    tls_versions = ["769", "770", "771", "772"] 
    cipher_suites = ["47-53-255", "46-49-150", "48-54-200"]
    extensions = ["0-23-65281-10-11", "0-19-65280-11-13", "0-20-65280-12-14"]
    curves= ["29-23", "28-21", "27-22", "29-23"]

    tls_ja3_templates = [
        "{version},{ciphers},{extensions},{curves}"
    ]

    ttl_values = [64, 128, 255]
    is_anomaly_values = [0, 1]

    # Generate the synthetic data
    data = {
        "user_agent": [],
        "tls_ja3": [],
        "ttl": [],
        "is_anomaly": []
    }

    for _ in range(num_records):
        # Randomly choose values for each field
        user_agent = random.choice(user_agents)

        tls_version = random.choice(tls_versions)
        cipher_suite = random.choice(cipher_suites)
        extension = random.choice(extensions)
        curve = random.choice(curves)
        tls_ja3 = tls_ja3_templates[0].format(
            version=tls_version,
            ciphers=cipher_suite,
            extensions=extension,
            curves=curve,
        )

        ttl = random.choice(ttl_values)
        is_anomaly = random.choice(is_anomaly_values)

        # Append the generated values to the corresponding lists
        data["user_agent"].append(user_agent)
        data["tls_ja3"].append(tls_ja3)
        data["ttl"].append(ttl)
        data["is_anomaly"].append(is_anomaly)

    return json.dumps(data, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic TLS data.")
    parser.add_argument("--num_samples", type=int, required=True, help="Number of samples to generate.")
    parser.add_argument("--seed", type=int, default=0, help="Random seed for reproducibility.")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    synthetic_data = generate_data(args.num_samples)
    output_file = "synthetic_tls_data.json"

    with open(output_file, "w") as f:
        f.write(synthetic_data)

    print(f"Synthetic data with {args.num_samples} samples has been written to {output_file}.")
