Bu proje, WiFi ağlarının sinyal gücünü taramak ve analiz etmek için Python tabanlı bir araçtır. Sisteminizdeki mevcut WiFi ağlarının SSID'lerini (ağ adları) ve sinyal güçlerini (Signal Strength) ölçerek listeleyen bir uygulama sunmaktadır. Kullanıcılar bu araç sayesinde çevredeki WiFi ağlarını izleyebilir ve güçlü sinyalleri bulabilir.

🚀 Başlangıç - Getting Started
Gereksinimler - Prerequisites
Bu proje, aşağıdaki araç ve kütüphanelerin yüklü olmasını gerektirir:

- Python 3.x
- "subprocess" (Python ile gelen standart kütüphane)
- re (Python ile gelen standart kütüphane)
- WiFi taraması yapmak için işletim sistemine bağlı komutlar:
  -Windows: netsh wlan show network
  -Linux/Mac: iwlist veya nmcli komutları
# Kurulum - Installation
## Adımlar - Steps
- Python'un en son sürümünü indirin ve kurun: Python.org
- Projeyi klonlayın veya indirin:
![code](https://github.com/user-attachments/assets/b213627f-238a-4e67-9cea-f8b263527b70)
- Python kütüphaneleri yüklemek için gerekli komutları çalıştırın (Bu projede standart kütüphaneler kullanıldığı için ekstra bir şey kurmanıza gerek yok).
- "python main.py && linux.py" komutunu çalıştırarak WiFi ağlarını tarayın.

# 📊 Çıktı - Output
Aşağıda, komut satırında çıkan örnek bir çıktı gösterilmektedir:

Örnek Çıktı - Example Output:
![Q](https://github.com/user-attachments/assets/e94bb98d-874f-4ebf-a184-cf313c1c1b04)

# 🎨 Özellikler - Features
- WiFi Tarama: Çevredeki WiFi ağlarını tarar.

- Sinyal Gücü Ölçümü: Her ağın sinyal gücünü ölçer ve gösterir.

- İşletim Sistemi Desteği: Hem Windows hem de Linux/Mac üzerinde çalışabilir.

- Kolay Kullanım: Tek komutla tüm ağlar taranır ve sinyal gücü hesaplanır.

# 🛠️ Katkıda Bulunma - Contributing
Bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

- Bu projeyi fork'layın.

- Yeni bir branch oluşturun (git checkout -b feature/xyz).

- Değişikliklerinizi yapın ve commit edin (git commit -am 'Add new feature').

- GitHub üzerinde pull request açın.

# 📄 Lisans - License
- Bu proje MIT Lisansı altında lisanslanmıştır - MIT Lisansı.

------------------------------------------------------------------
# English

This project is a Python-based tool to scan and analyze WiFi signal strength. It lists the SSIDs (network names) and signal strengths (Signal Strength) of available WiFi networks around your system. Users can monitor nearby WiFi networks and find the strongest signals using this tool.

🚀 Getting Started
Prerequisites
This project requires the following tools and libraries:

- Python 3.x
- subprocess (a standard Python library)
- re (a standard Python library)
- OS-dependent commands for WiFi scanning:
-   Windows: netsh wlan show network
-   Linux/Mac: iwlist or nmcli commands
# Installation
## Steps
- Download and install the latest version of Python: Python.org
- Clone or download the project:
- ![2](https://github.com/user-attachments/assets/6e9b15a3-9df9-4776-9874-3fc3c104304b)
- No additional libraries are required, as the project uses only standard Python libraries.
- Run python signal_finder.py to start scanning the WiFi networks.

# 📊 Output
Here’s an example of the output you might see:

Example Output:
![ee](https://github.com/user-attachments/assets/c8fc5453-c709-45e0-b9ba-3db43c3194a1)

# 🎨 Features
- WiFi Scanning: Scans for nearby WiFi networks.

- Signal Strength Measurement: Measures and displays the signal strength of each network.

- OS Support: Works on both Windows and Linux/Mac.

- Easy to Use: Just one command to scan networks and measure signal strength.

# 🛠️ Contributing
If you want to contribute to this project, please follow these steps:

- Fork this project.

- Create a new branch (git checkout -b feature/xyz).

- Make your changes and commit (git commit -am 'Add new feature').

- Open a pull request on GitHub.

# 📄 License

This project is licensed under the MIT License - MIT License.
