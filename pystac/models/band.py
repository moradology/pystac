from pystac.models.base import STACObject


class Band(STACObject):
    def __init__(self, common_name: str, gsd: float,
                 center_wavelength: float, effective_bandwidth: float,
                 image_band_index: int):
        """Band object used in product specifications

        Args:
            common_name (str): common, human readable name for band used in UIs
            gsd (float): ground sampling distance
            center_wavelength (float): central wavelength
            effective_bandwidth (float): bandwidth of band
            image_band_index (int): index of band in source file

        """
        self.common_name = common_name
        self.gsd = gsd
        self.center_wavelength = center_wavelength
        self.effective_bandwidth = effective_bandwidth
        self.image_band_index = image_band_index

    @property
    def dict(self):
        return dict(
            common_name=self.common_name,
            gsd=self.gsd,
            center_wavelength=self.center_wavelength,
            effective_bandwidth=self.effective_bandwidth,
            image_band_index=self.image_band_index
        )
