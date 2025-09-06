from load_image import ft_load


def main():
    """Test the ft_load function with a sample image."""
    try:
        bmi = ft_load("landscape.jpg")
        print(bmi)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
